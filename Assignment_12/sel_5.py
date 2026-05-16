from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.amazon.in")

time.sleep(3)
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("oppo k13 turbo")

driver.find_element(By.ID, "nav-search-submit-button").click()

time.sleep(3)

products = driver.find_elements(By.XPATH, "//h2/span")

print("Products Found:", len(products))

for product in products:
    print(product.text)

driver.quit()