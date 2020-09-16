from selenium import webdriver
import csv
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")

class eve_search:

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def search(self, url):
        driver = self.driver
        driver.get(url)
        product_names = [name.text for name in driver.find_elements_by_class_name('myProductName')]
        prices = [price.text for price in driver.find_elements_by_class_name('price')]
        links = [link.get_attribute('href') for link in driver.find_elements_by_link_text('More Info')]
        products = sorted(zip(product_names, prices, links))

        return product_names, prices, links
