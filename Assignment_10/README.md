# Amazon Price Tracer

## Description

Amazon Price Tracer is a Python-based web scraping application that extracts product titles and prices from Amazon product pages and compares the current price with a user-defined target price.

The application uses:

- `requests` for sending HTTP requests
- `BeautifulSoup` for HTML parsing and scraping

---

## Features

- Extract Amazon product titles
- Extract product prices
- Convert scraped prices into numeric values
- Compare current price with target price
- Handle missing titles or prices gracefully
- Test multiple product URLs in a single run

---

## Requirements

- Python 3.x
- requests
- beautifulsoup4

---

## Installation

Clone the repository or download the project files.

Install required packages:

```bash
pip install requests beautifulsoup4
```

---

## Project Structure

```bash
amazon-price-tracer/
│
├── pricetracker.py
├── example.py
├── README.md
├── requirements.txt
└── screenshots/
    ├── code.png
    └── output.png
```

---

## How It Works

The application:

1. Sends an HTTP request to the Amazon product page
2. Extracts:
   - Product title
   - Product price
3. Cleans the price string by removing:
   - Currency symbols
   - Commas
4. Converts the price into a float value
5. Compares the current price with the target price

---

## Example Product List

```python
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
```

---

## Run the Application

```bash
python example.py
```

---

## Example Output

```bash

==================================================
Product: OPPO K13 Turbo 5G, Purple Phantom (8GB, 128GB)
Current Price: 28,890.
Target Price: ₹25000
Price is above target price

==================================================
Product: Lenovo LOQ 13th Gen Intel Core i7-13650HX 15.6" (39.6cm) 144Hz 300Nits FHD Gaming Laptop (16GB/512GB SSD/Win 11/NVIDIA RTX 4050 6GB/1Yr ADP Free/MSO 24/Grey/2.3Kg), 83DV01A5IN
Current Price: 1,04,990.
Target Price: ₹110000
Price is below target price

==================================================
Product: HP KM300F Wired USB Gaming Keyboard and Mouse Set, Membrane Backlit, 26 Keys Anti-Ghosting, 3 LED Indicators & 3D 6K USB Mouse with 6400DPI,Six-Speed Cyclic Resolution Switching, Black
Current Price: 1,399.
Target Price: ₹1500
Price is below target price
```

---

## Price Comparison Logic

The application compares prices using the `compare_price()` method.

Possible results:

- `above`
- `below`
- `equal`

---

## Error Handling

The application handles edge cases such as:

- Product title not found
- Product price not found
- Invalid HTML structure
- Amazon page structure variations

Fallback selectors are used to improve scraping reliability.

---

## Screenshots

Add screenshots inside the `screenshots/` folder showing:

1. Source code
2. Terminal execution output

Example:

```bash
screenshots/code.png
screenshots/output.png
```