import requests
from bs4 import BeautifulSoup

def fetch_basic_product(url):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/148.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find("span", id="productTitle")
    price = soup.find("span", class_="a-price-whole")

    title_text = title.get_text(strip=True) if title else "Title not found"
    price_text = price.get_text(strip=True) if price else "Price not found"

    return title_text, price_text



def clean_price(price_text):

    # Remove currency symbol and commas
    cleaned = (
        price_text
        .replace("₹", "")
        .replace(",", "")
        .strip()
    )

    return float(cleaned)

def compare_price(current_price, target_price):

    if current_price > target_price:
        return "above"

    if current_price < target_price:
        return "below"

    return "equal"


def fetch_with_fallbacks(url):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/148.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    # Title extraction
    title_element = soup.find("span", id="productTitle")

    title = (
        title_element.get_text(strip=True)
        if title_element
        else "Title not found"
    )

    # Different Amazon pages expose prices differently.
    # We'll try multiple selectors in sequence.
    price_selectors = [
        ("span", {"class": "a-price-whole"}),
        ("span", {"class": "a-offscreen"}),
        ("span", {"id": "priceblock_ourprice"}),
        ("span", {"id": "priceblock_dealprice"})
    ]

    price = None

    for tag, attrs in price_selectors:

        # Try current selector
        element = soup.find(tag, attrs=attrs)

        # Stop once a valid price is found
        if element:
            price = element.get_text(strip=True)
            break

    if not price:
        price = "Price not found"

    return title, price



def safe_fetch_product(url):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/148.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        title_element = soup.find("span", id="productTitle")

        title = (
            title_element.get_text(strip=True)
            if title_element
            else "Title not found"
        )

        price_selectors = [
            ("span", {"class": "a-price-whole"}),
            ("span", {"class": "a-offscreen"}),
            ("span", {"id": "priceblock_ourprice"}),
            ("span", {"id": "priceblock_dealprice"})
        ]

        price = None

        for tag, attrs in price_selectors:

            element = soup.find(tag, attrs=attrs)

            if element:
                price = element.get_text(strip=True)
                break

        if not price:
            return title, "Price not found"

        return title, price

    except requests.exceptions.Timeout:
        return "Request failed", "Timeout"

    except requests.exceptions.HTTPError as err:
        return "HTTP error", str(err)

    except requests.exceptions.RequestException as err:
        return "Network error", str(err)

    except Exception as err:
        # Catch unexpected parsing issues
        return "Unknown error", str(err)


class PriceTracer:

    def __init__(self, url):

        self.url = url

        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/148.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9"
        }

        # Centralized selector registry.
        # Easy to extend later.
        self.price_selectors = [
            ("span", {"class": "a-price-whole"}),
            ("span", {"class": "a-offscreen"}),
            ("span", {"id": "priceblock_ourprice"}),
            ("span", {"id": "priceblock_dealprice"})
        ]

    def fetch_page(self):

        response = requests.get(
            self.url,
            headers=self.headers,
            timeout=10
        )

        response.raise_for_status()

        return BeautifulSoup(response.content, "html.parser")

    def extract_title(self, soup):

        element = soup.find("span", id="productTitle")

        if not element:
            return "Title not found"

        return element.get_text(strip=True)

    def extract_price(self, soup):

        # Try selectors one by one.
        # First successful match wins.
        for tag, attrs in self.price_selectors:

            element = soup.find(tag, attrs=attrs)

            if element:
                return element.get_text(strip=True)

        return "Price not found"

    def clean_price(self, price_text):

        try:
            return float(
                price_text
                .replace("₹", "")
                .replace(",", "")
                .strip()
            )

        except ValueError:
            return None

    def compare_price(self, current_price, target_price):

        current = self.clean_price(current_price)

        if current is None:
            return "invalid price"

        if current > target_price:
            return "above"

        if current < target_price:
            return "below"

        return "equal"

    def fetch_product(self):

        try:

            soup = self.fetch_page()

            title = self.extract_title(soup)
            price = self.extract_price(soup)

            return title, price

        except requests.exceptions.RequestException as err:
            return "Network issue", str(err)

        except Exception as err:
            return "Unexpected error", str(err)



products = [
    {
        "url": "https://www.amazon.in/OPPO-K13-Turbo-5G-Phantom/dp/B0FNLRR81F",
        "target_price": 25000
    },
    {
        "url": "https://www.amazon.in/Lenovo-i7-13650HX-39-6cm-300Nits-83DV01A5IN/dp/B0G3B47HZF/",
        "target_price": 110000
    }
]


for item in products:

    print("\n" + "=" * 50)

    tracker = PriceTracer(item["url"])

    title, price = tracker.fetch_product()

    print(f"Product: {title}")
    print(f"Current Price: ₹{price}")

    if price != "Price not found":

        result = tracker.compare_price(
            price,
            item["target_price"]
        )

        print(f"Target Price: ₹{item['target_price']}")
        print(f"Price is {result} target price")

    else:
        print("Could not compare price.")