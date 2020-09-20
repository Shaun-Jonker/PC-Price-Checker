from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ProductSearch:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def eve_search(self, website):
        self.driver.get(website)

        print('Running Evetech in headless mode')

        product_names = [name.text for name in self.driver.find_elements_by_class_name('myProductName')]
        prices = [price.text for price in self.driver.find_elements_by_class_name('price')]
        links = [link.get_attribute('href') for link in self.driver.find_elements_by_link_text('More Info')]

        products = sorted(zip(product_names, prices, links))

        return products

    def woot_search(self, website):
        self.driver.get(website)

        print('Running Wootware in headless mode')

        woot_name = [n.text for n in self.driver.find_elements_by_class_name('product-name')]
        woot_price = [p.text for p in self.driver.find_elements_by_class_name('price')]
        woot_saving = [s.text for s in self.driver.find_elements_by_class_name('special-price-saving')]
        woot_elems = self.driver.find_elements_by_css_selector(".products-grid .product-name a")
        woot_links = [elem.get_attribute('href') for elem in woot_elems]
        print(f"Found {len(woot_name)} Mouse Products")
        print("Finished Wootware Mouse Collection")

        woot_products = sorted(zip(woot_name, woot_price, woot_saving, woot_links))

        return woot_products
