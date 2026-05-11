import requests
from bs4 import BeautifulSoup


class PriceTracer:

    def __init__(self, url):

        self.url = url
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
                        "Accept-Language": "en-US,en;q=0.9"
        }
    def fetch_product(self):

        response = requests.get(
            self.url,
            headers=self.headers
        )

        soup = BeautifulSoup(response.content, "html.parser")

        # Product title
        title = soup.find("span", id="productTitle")

        if title:
            title = title.get_text(strip=True)
        else:
            title = "Title not found"

        price = None

        selectors = [
            ("span", {"class": "a-price-whole"}),
            ("span", {"class": "a-offscreen"}),
        ]

        for tag, attrs in selectors:

            price_element = soup.find(tag, attrs=attrs)

            if price_element:
                price = price_element.get_text(strip=True)
                break

        if not price:
            price = "Price not found"

        return title, price

    def clean_price(self, price_text):

        return float(
            price_text.replace("₹", "")
                      .replace(",", "")
                      .strip()
        )

    def compare_price(self, current_price, target_price):

        current_price = self.clean_price(current_price)

        if current_price > target_price:
            return "above"

        elif current_price < target_price:
            return "below"

        return "equal"


products = [

    {
        "url": "https://www.amazon.in/OPPO-K13-Turbo-5G-Phantom/dp/B0FNLRR81F",
        "target_price": 25000
    },

    {
        "url": "https://www.amazon.in/Lenovo-i7-13650HX-39-6cm-300Nits-83DV01A5IN/dp/B0G3B47HZF/",
        "target_price": 110000
    },

    {
        "url": "https://www.amazon.in/HP-KM300F-Gaming-Keyboard-8AA01AA/dp/B0849859X1/",
        "target_price": 1500
    }

]


for item in products:

    print("\n" + "=" * 50)

    url = item["url"]
    target_price = item["target_price"]

    tracker = PriceTracer(url)

    title, price = tracker.fetch_product()

    print(f"Product: {title}")
    print(f"Current Price: {price}")

    if price != "Price not found":

        result = tracker.compare_price(price, target_price)

        print(f"Target Price: ₹{target_price}")
        print(f"Price is {result} target price")

    else:
        print("Could not compare price.")

