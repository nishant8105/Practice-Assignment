# Amazon Price Tracker 🛒📉

This project is a simple Amazon price tracker built using Python, `requests`, and `BeautifulSoup`.

I built this project to learn how web scraping works in real-world scenarios. The main idea was to automatically fetch product details from Amazon pages, extract the current product price, and compare it with a target price that I define myself.

Instead of hardcoding everything in one function, I gradually improved the project step by step:

- first by scraping a single product
- then by cleaning the extracted price
- then by handling missing price formats
- then by adding error handling
- and finally by creating a reusable `PriceTracer` class

The final version can track multiple products and tell me whether the current price is above or below my target price.

---

# What This Project Does ⚙️

The script:

- sends an HTTP request to an Amazon product page
- extracts:
  - product title
  - current product price
- cleans the price into a usable number
- compares it against a target price
- prints whether the price is:
  - above target
  - below target
  - equal to target

I also added fallback selectors because Amazon pages don't always use the same HTML structure for prices.

---

# Features 🚀

## Basic Product Scraping

Fetches:

- Product title
- Product price

using:

```python
requests
BeautifulSoup
```

---

## Price Cleaning

Converts prices like:

```text
₹1,24,999
```

into:

```python
124999.0
```

so numerical comparison becomes possible.

---

## Multiple Price Selectors

Amazon changes its page structure frequently, so I added fallback selectors like:

```python
a-price-whole
a-offscreen
priceblock_ourprice
priceblock_dealprice
```

This makes the scraper more reliable.

---

## Error Handling 🛡️

The project handles:

- network failures
- request timeouts
- HTTP errors
- invalid parsing cases

instead of crashing immediately.

---

## Object-Oriented Version

I created a `PriceTracer` class to organize the logic better.

The class handles:

- fetching pages
- extracting titles
- extracting prices
- cleaning prices
- comparing prices

This made the code much cleaner and easier to extend later.

---

# Technologies Used 🧰

- Python
- Requests
- BeautifulSoup4

---

# Project Structure 📂

```text
price_tracker.py
```

Everything is currently inside one file.

The flow is roughly:

```text
Fetch Page
   ↓
Parse HTML
   ↓
Extract Title + Price
   ↓
Clean Price
   ↓
Compare With Target
   ↓
Print Result
```

---

# How I Run This Project ▶️

## 1. Install Dependencies

These are the packages I installed:

```bash
pip install requests beautifulsoup4
```
---

## 2. Run the Script

This is the actual command I use:

```bash
python price_tracker.py
```
```bash
python3 price_tracker.py
```
---

# Products I Tested

I tested the tracker using:

- OPPO K13 Turbo 5G
- Lenovo Gaming Laptop

with different target prices.

---

# What I Learned 📚

While building this project, I learned:

- how HTTP requests work
- how websites structure HTML
- how web scraping works with BeautifulSoup
- why scraping real websites is unreliable sometimes
- how to write cleaner Python using classes
- how to handle exceptions properly

I also learned that Amazon pages are inconsistent, which is why fallback selectors and error handling are important.

---
