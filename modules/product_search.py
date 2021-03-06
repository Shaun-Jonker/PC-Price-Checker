from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class ProductSearch:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=chrome_options)

    def eve_search(self, website, item_name):
        self.driver.get(website)

        print('Running Evetech in headless mode')

        product_names = [name.text for name in self.driver.find_elements_by_class_name('myProductName')]
        prices = [price.text for price in self.driver.find_elements_by_class_name('price')]
        links = [link.get_attribute('href') for link in self.driver.find_elements_by_link_text('More Info')]
        print(f"Found {len(product_names)} {item_name} Products")

        products = sorted(zip(product_names, prices, links))
        print(f"Finished Evetech {item_name} Collection\n")
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
        print(f"Finished Wootware {item_name} Collection\n")

        return woot_products

    def foxy_search(self, website, item_name):

        self.driver.get(website)
        print('Running Foxytech in headless mode')
        element = self.driver.find_element_by_name('ppp')
        element.click()

        for i in range(4):
            element.send_keys(Keys.ARROW_DOWN)

        element.click()

        foxy_names = [p.text.strip('') for p in self.driver.find_elements_by_class_name("woocommerce-loop-product__title")]

        foxy_name = []
        for name in foxy_names:
            if name == '':
                continue
            foxy_name.append(name)
        
        foxy_price = [price.text for price in self.driver.find_elements_by_class_name("price")]
        foxy_links = [l.get_attribute("href") for l in self.driver.find_elements_by_css_selector(".owl-item>.product .woocommerce-LoopProduct-link, .products>.product .woocommerce-LoopProduct-link")]
        foxy_link = list(dict.fromkeys(foxy_links))

        print(f"Found {len(foxy_name)} {item_name} Products")

        foxy_products = sorted(zip(foxy_name, foxy_price, foxy_link))

        print(f"Finished Foxytexh {item_name} Collection\n")


        return foxy_products

    def titan_search(self, website, item_name):

        self.driver.get(website + "?features_hash=174-Y&items_per_page=96")
        print('Running TitanIce in headless mode')

        titanice_names = [name.get_attribute('title') for name in self.driver.find_elements_by_class_name('product-title')]
        titanice_price = [price.text for price in self.driver.find_elements_by_class_name('ty-grid-list__price')]
        titanice_links =[link.get_attribute('href') for link in self.driver.find_elements_by_class_name('product-title')]

        print(f"Found {len(titanice_names)} {item_name} Products")

        titanice_products = sorted(zip(titanice_names, titanice_price, titanice_links))

        print(f"Finished TitanIce {item_name} Collection\n")

        return titanice_products
