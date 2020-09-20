from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class ProductSearch:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)

    def eve_search(self, website, item_name):
        self.driver.get(website)

        print('Running Evetech in headless mode')

        product_names = [name.text for name in self.driver.find_elements_by_class_name('myProductName')]
        prices = [price.text for price in self.driver.find_elements_by_class_name('price')]
        links = [link.get_attribute('href') for link in self.driver.find_elements_by_link_text('More Info')]
        print(f"Found {len(product_names)} {item_name} Products")

        products = sorted(zip(product_names, prices, links))
        print(f"Finished Evetech {item_name} Collection")
        return products

    def woot_search(self, website, item_name):
        self.driver.get(website)

        print('Running Wootware in headless mode')

        woot_name = [n.text for n in self.driver.find_elements_by_class_name('product-name')]
        woot_price = [p.text for p in self.driver.find_elements_by_class_name('price')]
        woot_saving = [s.text for s in self.driver.find_elements_by_class_name('special-price-saving')]
        woot_elems = self.driver.find_elements_by_css_selector(".products-grid .product-name a")
        woot_links = [elem.get_attribute('href') for elem in woot_elems]

        print(f"Found {len(woot_name)} {item_name} Products")

        woot_products = sorted(zip(woot_name, woot_price, woot_saving, woot_links))
        print(f"Finished Wootware {item_name} Collection")

        return woot_products

    def foxy_search(self, website, item_name):
        foxy_options = Options()
        foxy_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=foxy_options)

        self.driver.get(website)

        print('Running Foxy in headless mode')
        
        self.driver.implicitly_wait(10)

        element = self.driver.find_element_by_name('ppp')
        
        self.driver.implicitly_wait(2)
        element.click()

        for i in range(4):
            element.send_keys(Keys.ARROW_DOWN)
            self.driver.implicitly_wait(1.5)

        element.click()
        print("I got here")
        foxy_name = [p.text for p in self.driver.find_elements_by_class_name("woocommerce-loop-product__title")]
        foxy_price = [price.text for price in self.driver.find_elements_by_class_name("price")]
        foxy_link = [l.get_attribute("href") for l in self.driver.find_elements_by_class_name('woocommerce-LoopProduct-link')]

        print(foxy_name)
        print(foxy_price)
        print(foxy_link)

        foxy_products = sorted(zip(foxy_name, foxy_price, foxy_link))

        self.driver.close()

        return foxy_products