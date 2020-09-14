from selenium import webdriver
import csv
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")


class Evetech:

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def ssd(self):
        driver = self.driver
        driver.get("https://www.evetech.co.za/PC-Components/buy-solid-state-drives-83.aspx")
        print('Running Evetech in headless mode')

        product_names = [name.text for name in driver.find_elements_by_class_name('myProductName')]
        prices = [price.text for price in driver.find_elements_by_class_name('price')]
        links = [link.get_attribute('href') for link in driver.find_elements_by_link_text('More Info')]
        print(f'Found {len(product_names)} SSD Products')
        print("Finished Evetech SSD Collection")
        print('Writing to file')

        products = sorted(zip(product_names, prices, links))

        with open('SSD.csv', "w", newline='') as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in products:
                writer.writerow(item)
        print("=====Writing to file complete=====\n")

    def graphics_cards(self):
        driver = self.driver
        driver.get("https://www.evetech.co.za/components/nvidia-ati-graphics-cards-21.aspx")
        print('Running Evetech in headless mode')

        product_names = [name.text for name in driver.find_elements_by_class_name('myProductName')]
        prices = [price.text for price in driver.find_elements_by_class_name('price')]
        links = [link.get_attribute('href') for link in driver.find_elements_by_link_text('More Info')]
        print(f'Found {len(product_names)} Graphics Card Products')
        print("Finished Evetech Graphics Card Collection")
        print('Now writing to file')

        products = sorted(zip(product_names, prices, links))

        with open('Graphics Cards.csv', "w", newline='') as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in products:
                writer.writerow(item)
        print("=====Writing to file complete=====\n")



