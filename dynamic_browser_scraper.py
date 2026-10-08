from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Configure headless chrome parameters for cloud execution
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--remote-debugging-port=9222')

driver = webdriver.Chrome(options=options)

# Target the dynamic JavaScript training sandbox
target_url = "https://webscraper.io"
driver.get(target_url)

# Allow script arrays to completely render components into the DOM structure
time.sleep(4)

laptop_cards = driver.find_elements(By.CLASS_NAME, 'thumbnail')
names = []
prices = []

for card in laptop_cards:
    names.append(card.find_element(By.CLASS_NAME, 'title').text)
    prices.append(card.find_element(By.CLASS_NAME, 'price').text)

df_dynamic_data = pd.DataFrame({'Laptop_Model': names, 'Rendered_Price': prices})
print("--- Dynamic Browser Automation Scraper Executed Safely ---")
print(df_dynamic_data.head())

driver.quit()
