from selenium import webdriver
import csv
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")


class Wootware:

    def __init__(self):
        self.wootware = webdriver.Chrome(options=chrome_options)

    def ssd(self):
        self.wootware.get("https://www.wootware.co.za/computer-hardware/hard-drives-ssds/solid-state-disks/shopby"
                          "/in_stock_with_wootware?limit=500")
        print('Running Wootware in headless mode')

        woot_name = [n.text for n in self.wootware.find_elements_by_class_name('product-name')]
        woot_price = [p.text for p in self.wootware.find_elements_by_class_name('price')]
        woot_saving = [s.text for s in self.wootware.find_elements_by_class_name('special-price-saving')]
        woot_elems = self.wootware.find_elements_by_css_selector(".products-grid .product-name a")
        woot_links = [elem.get_attribute('href') for elem in woot_elems]
        print(f"Found {len(woot_name)} SSD Products")
        print("Finished Wootware Collection")
        print('Now writing to file')

        woot_products = sorted(zip(woot_name, woot_price, woot_saving, woot_links))

        with open('SSD.csv', "a+", newline='') as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in woot_products:
                writer.writerow(item)

        print("=====Writing to file complete=====\n")

    def graphics_cards(self):
        self.wootware.get("https://www.wootware.co.za/computer-hardware/video-cards-video-devices/shopby"
                          "/in_stock_with_wootware?limit=100")
        print('Running Wootware in headless mode')

        woot_name = [n.text for n in self.wootware.find_elements_by_class_name('product-name')]
        woot_price = [p.text for p in self.wootware.find_elements_by_class_name('price')]
        woot_saving = [s.text for s in self.wootware.find_elements_by_class_name('special-price-saving')]
        woot_elems = self.wootware.find_elements_by_css_selector(".products-grid .product-name a")
        woot_links = [elem.get_attribute('href') for elem in woot_elems]
        print(f"Found {len(woot_name)} Graphics Card Products")
        print("Finished Wootware Collection")
        print('Now writing to file')

        woot_products = sorted(zip(woot_name, woot_price, woot_saving, woot_links))

        with open('Graphics Cards.csv', "a+", newline='') as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in woot_products:
                writer.writerow(item)

        print("=====Writing to file complete=====\n")



