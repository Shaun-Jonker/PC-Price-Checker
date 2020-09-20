from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ProductSearch:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def eve_search(self, website):
        self.driver.get(website)

        product_names = [name.text for name in self.driver.find_elements_by_class_name('myProductName')]
        prices = [price.text for price in self.driver.find_elements_by_class_name('price')]
        links = [link.get_attribute('href') for link in self.driver.find_elements_by_link_text('More Info')]

        products = sorted(zip(product_names, prices, links))

        return products
