# Assignment 12 - Selenium Practice

This folder contains simple Selenium automation scripts using Python and Chrome WebDriver.

## Files

- `sel_1.py`
  - Opens `https://www.google.com`
  - Searches for `selenium`
  - Clicks the search button
  - Navigates back and forward
  - Closes the browser

- `sel_2.py`
  - Same flow as `sel_1.py`
  - Also maximizes the browser window before searching

- `sel_3.py`
  - Opens `https://www.amazon.in`
  - Maximizes the browser window
  - Clicks the `Electronics` link
  - Clicks the `Audio` link

- `sel_4.py`
  - Opens `https://www.google.com`
  - Maximizes the browser window
  - Waits and refreshes the page

- `sel_5.py`
  - Opens `https://www.amazon.in`
  - Maximizes the browser window
  - Searches for `oppo k13 turbo`
  - Prints the number of product listings found
  - Prints each product title in the search results

## Requirements

- Python 3.x
- `selenium` Python package
- Chrome browser installed
- ChromeDriver compatible with your Chrome version

## Setup

1. Create and activate a Python virtual environment (optional):

```bash
python -m venv .venv
.venv\Scripts\activate 
```

2. Install Selenium:

```bash
pip install selenium
```

3. Make sure `chromedriver.exe` is installed and available on your PATH, or place it in the same folder as the script.

## Run a script

From the `Assignment_12` folder, run:

```bash
python sel_1.py
```

Replace `sel_1.py` with the desired script file name.
