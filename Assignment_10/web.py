import urllib.request

import requests
from bs4 import BeautifulSoup

import csv
import re
import os


# ============================================================
# 1. URL OPEN USING urllib
# ============================================================

print("\n================ urllib Example ================\n")

url = urllib.request.urlopen('http://127.0.0.1:5000/')

for line in url:
    print(line.decode().strip())


# ============================================================
# 2. IMAGE DOWNLOAD USING requests
# ============================================================

print("\n================ Image Download ================\n")

image_url = 'http://127.0.0.1:5000/static/images/green.jpg'

headers = {
    'User-Agent': 'Mozilla/5.0'
}

response = requests.get(url=image_url, headers=headers)

print(response)
print(response.status_code)
print(response.headers)
print(response.request.headers)

# Save Image
with open('green.jpg', 'wb') as file:
    file.write(response.content)

print("Image Downloaded Successfully")


# ============================================================
# 3. SIMPLE GET REQUEST
# ============================================================

print("\n================ GET Request ================\n")

url = 'http://127.0.0.1:5000/'

response = requests.get(url=url)

print(response.text)
print(type(response.text))


# ============================================================
# 4. POST REQUEST
# ============================================================

print("\n================ POST Request ================\n")

url = 'http://127.0.0.1:8000/api/users/'

params = {
    "offset": "10",
}

payload = {
    "bio": "Some thing",
    "profile_picture": "green.jpg",
    "phone": 89878987899,
    "location": "mumbai"
}

response = requests.post(url=url, data=payload)

print(response.text)

response = requests.post(url=url, params=params)

print(response.text)


# ============================================================
# 5. WEB SCRAPING & CSV
# ============================================================

print("\n================ Web Scraping ================\n")

wiki_url = "https://en.wikipedia.org/wiki/Main_Page"

headers = {
    "User-Agent": "Mozilla/5.0"
}


def extract_data(url):

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    tag = soup.find("div", id="mp-right")

    h1 = tag.find("h2")

    h2 = tag.find_all("h2")

    content = [span.text.strip() for span in h2]

    # Save CSV
    with open("wiki.csv", 'w', newline='', encoding='utf-8') as csv_file:

        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(["Headings"])

        for item in content:
            csv_writer.writerow([item])

    return tag, h1, h2, content


tag, h1, h2, content = extract_data(wiki_url)

print(tag)
print(h1)
print(h2)
print(content)


# ============================================================
# 6. IMAGE DOWNLOADER
# ============================================================

print("\n================ Image Downloader ================\n")

search = input("Enter Image Name: ")

headers = {
    'User-Agent': 'Mozilla/5.0'
}

url = f"https://www.bing.com/images/search?q={search}"

response = requests.get(url=url, headers=headers)

pattern = r'https://[^"]+\.(?:jpg|jpeg|png)'

images = re.findall(pattern, response.text)

# Remove duplicates
images = list(set(images))

print(f"Total Images Found: {len(images)}")

no_of_images = int(input("Enter Number of Images to Download: "))

# Create Folder
if not os.path.exists(search):
    os.mkdir(search)

for index, image_url in enumerate(images[:no_of_images]):

    try:

        image_data = requests.get(image_url).content

        image_name = f"image_{index + 1}.jpg"

        image_path = os.path.join(search, image_name)

        with open(image_path, 'wb') as file:
            file.write(image_data)

        print(f"{image_name} Downloaded")

    except Exception as e:
        print("Error:", e)


# ============================================================
# 7. AMAZON PRICE TRACKER
# ============================================================

print("\n================ Price Tracker ================\n")


class PriceTracer:

    def __init__(self, url):

        self.url = url

        self.headers = {
            'User-Agent': 'Mozilla/5.0'
        }

        self.response = requests.get(
            url=self.url,
            headers=self.headers
        )

        self.soup = BeautifulSoup(
            self.response.text,
            "lxml"
        )

    def product_title(self):

        title = self.soup.find(
            "span",
            {"id": "productTitle"}
        )

        if title is not None:
            return title.text.strip()

        return "Title Not Found"

    def product_price(self):

        price = self.soup.find(
            "span",
            {"class": "a-price-whole"}
        )

        if price is not None:
            return price.text.strip()

        return "Price Not Found"


device = PriceTracer(
    url="https://www.amazon.in/gp/aw/d/B0FJFSDYVC/"
)

print("Product Name:")
print(device.product_title())

print("\nProduct Price:")
print(device.product_price())

