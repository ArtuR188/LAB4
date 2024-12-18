import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'https://www.amazon.com/s?k=electronics'
driver.get(url)

time.sleep(3)

products = []

items = driver.find_elements(By.CSS_SELECTOR, '.s-main-slot .s-result-item')

for item in items:
    try:
        title = item.find_element(By.CSS_SELECTOR, 'h2').text
        price = item.find_element(By.CSS_SELECTOR, '.a-price-whole').text if item.find_elements(By.CSS_SELECTOR, '.a-price-whole') else "N/A"
        sales = item.find_element(By.CSS_SELECTOR, '.a-size-small .a-color-base').text if item.find_elements(By.CSS_SELECTOR, '.a-size-small .a-color-base') else "N/A"
        stock = item.find_element(By.CSS_SELECTOR, '.a-declarative .a-size-small').text if item.find_elements(By.CSS_SELECTOR, '.a-declarative .a-size-small') else "In Stock"

        products.append([title, price, sales, stock])

    except Exception:
        continue

with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name', 'Price', 'Sales', 'Stock'])
    for product in products:
        writer.writerow(product)

driver.quit()

print("Data saved to 'products.csv'.")
