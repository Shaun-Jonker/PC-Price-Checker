from selenium import webdriver
import csv
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")


class Foxytech:

    def __init__(self):
        self.foxytech = webdriver.Chrome(options=chrome_options)

    def ssd(self):
        self.foxytech.get("https://www.wootware.co.za/computer-hardware/hard-drives-ssds/solid-state-disks/shopby"
                          "/in_stock_with_wootware?limit=500")
        print('Running Wootware in headless mode')

        foxy_name = [n.text for n in self.foxytech.find_elements_by_class_name('product-name')]
        foxy_price = [p.text for p in self.foxytech.find_elements_by_class_name('price')]
        foxy_saving = [s.text for s in self.foxytech.find_elements_by_class_name('special-price-saving')]
        foxy_elems = self.foxytech.find_elements_by_css_selector(".products-grid .product-name a")
        foxy_links = [elem.get_attribute('href') for elem in woot_elems]
        print(f"Found {len(foxy_name)} SSD Products")
        print("Finished Wootware Collection")
        print('Now writing to file')

        foxy_products = sorted(zip(woot_name, woot_price, woot_saving, woot_links))

        with open('Price Lists/SSD.csv', "a+", newline='') as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in foxy_products:
                writer.writerow(item)

        print("=====Writing to file complete=====\n")

    def graphics_cards(self):
        self.foxytech.get("https://www.wootware.co.za/computer-hardware/video-cards-video-devices/shopby"
                          "/in_stock_with_wootware?limit=100")
        print('Running Wootware in headless mode')

        foxy_name = [n.text for n in self.foxytech.find_elements_by_class_name('product-name')]
        foxy_price = [p.text for p in self.foxytech.find_elements_by_class_name('price')]
        foxy_saving = [s.text for s in self.foxytech.find_elements_by_class_name('special-price-saving')]
        foxy_elems = self.foxytech.find_elements_by_css_selector(".products-grid .product-name a")
        foxy_links = [elem.get_attribute('href') for elem in foxy_elems]
        print(f"Found {len(foxy_name)} Graphics Card Products")
        print("Finished Wootware Collection")
        print('Now writing to file')

        foxy_products = sorted(zip(foxy_name, foxy_price, foxy_saving, foxy_links))

        with open('Price Lists/Graphics Cards.csv', "a+", newline='') as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in foxy_products:
                writer.writerow(item)

        print("=====Writing to file complete=====\n")

    def monitors(self):
        self.foxytech.get("https://www.wootware.co.za/computer-hardware/lcds-monitors/shopby/in_stock_with_wootware")
        print('Running Wootware in headless mode')

        woot_name = [n.text for n in self.foxytech.find_elements_by_class_name('product-name')]
        woot_price = [p.text for p in self.foxytech.find_elements_by_class_name('price')]
        woot_saving = [s.text for s in self.foxytech.find_elements_by_class_name('special-price-saving')]
        woot_elems = self.foxytech.find_elements_by_css_selector(".products-grid .product-name a")
        woot_links = [elem.get_attribute('href') for elem in woot_elems]
        print(f"Found {len(woot_name)} Monitors Products")
        print("Finished Wootware Monitors Collection")
        print('Now writing to file')

        woot_products = sorted(zip(woot_name, woot_price, woot_saving, woot_links))

        with open('Price Lists/Monitors.csv', "a+", newline='') as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in woot_products:
                writer.writerow(item)

        print("=====Writing to file complete=====\n")

    def keyboards(self):
        self.foxytech.get("https://www.wootware.co.za/computer-hardware/input-keyboards-mice-game-controllers-remotes"
                          "/keyboards/shopby/in_stock_with_wootware?gclid"
                          "=Cj0KCQjwqfz6BRD8ARIsAIXQCf2zGb4QGtS8U1zkGhSLbEx8NKQrinNeWUCJAiV67sCXqB7TuSbsMmkaAsc7EALw_wcB")
        print('Running Wootware in headless mode')

        woot_name = [n.text for n in self.foxytech.find_elements_by_class_name('product-name')]
        woot_price = [p.text for p in self.foxytech.find_elements_by_class_name('price')]
        woot_saving = [s.text for s in self.foxytech.find_elements_by_class_name('special-price-saving')]
        woot_elems = self.foxytech.find_elements_by_css_selector(".products-grid .product-name a")
        woot_links = [elem.get_attribute('href') for elem in woot_elems]
        print(f"Found {len(woot_name)} Keyboard Products")
        print("Finished Wootware Keyboard Collection")
        print('Now writing to file')

        woot_products = sorted(zip(woot_name, woot_price, woot_saving, woot_links))

        with open('Price Lists/Keyboards.csv', "a+", newline='') as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in woot_products:
                writer.writerow(item)

        print("=====Writing to file complete=====\n")

    def mice(self):
        self.foxytech.get("https://www.wootware.co.za/computer-hardware/input-keyboards-mice-game-controllers-remotes"
                          "/mice/shopby/in_stock_with_wootware")
        print('Running Wootware in headless mode')

        woot_name = [n.text for n in self.foxytech.find_elements_by_class_name('product-name')]
        woot_price = [p.text for p in self.foxytech.find_elements_by_class_name('price')]
        woot_saving = [s.text for s in self.foxytech.find_elements_by_class_name('special-price-saving')]
        woot_elems = self.foxytech.find_elements_by_css_selector(".products-grid .product-name a")
        woot_links = [elem.get_attribute('href') for elem in woot_elems]
        print(f"Found {len(woot_name)} Mouse Products")
        print("Finished Wootware Mouse Collection")
        print('Now writing to file')

        woot_products = sorted(zip(woot_name, woot_price, woot_saving, woot_links))

        with open('Price Lists/Mouses.csv', "a+", newline='') as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in woot_products:
                writer.writerow(item)

        print("=====Writing to file complete=====\n")

    def cpu(self):
        self.foxytech.get("https://www.wootware.co.za/computer-hardware/input-keyboards-mice-game-controllers-remotes"
                          "/mice/shopby/in_stock_with_wootware")
        print('Running Wootware in headless mode')

        woot_name = [n.text for n in self.foxytech.find_elements_by_class_name('product-name')]
        woot_price = [p.text for p in self.foxytech.find_elements_by_class_name('price')]
        woot_saving = [s.text for s in self.foxytech.find_elements_by_class_name('special-price-saving')]
        woot_elems = self.foxytech.find_elements_by_css_selector(".products-grid .product-name a")
        woot_links = [elem.get_attribute('href') for elem in woot_elems]
        print(f"Found {len(woot_name)} CPU Products")
        print("Finished Wootware CPU Collection")
        print('Now writing to file')

        woot_products = sorted(zip(woot_name, woot_price, woot_saving, woot_links))

        with open('Price Lists/CPU.csv', "a+", newline='') as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in woot_products:
                writer.writerow(item)

        print("=====Writing to file complete=====\n")