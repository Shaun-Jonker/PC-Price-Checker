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

        with open('../Price Lists/SSD.csv', "w", newline='') as the_file:
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

        with open('../Price Lists/Graphics Cards.csv', "w", newline='') as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in products:
                writer.writerow(item)
        print("=====Writing to file complete=====\n")

    def monitors(self):
        driver = self.driver
        driver.get('https://www.evetech.co.za/PC-Components/pc-monitors-89.aspx')

        print('Running Evetech in headless mode')

        product_names = [name.text for name in driver.find_elements_by_class_name('myProductName')]
        prices = [price.text for price in driver.find_elements_by_class_name('price')]
        links = [link.get_attribute('href') for link in driver.find_elements_by_link_text('More Info')]
        print(f'Found {len(product_names)} Monitors Products')
        print("Finished Evetech Monitors Collection")
        print('Now writing to file')

        products = sorted(zip(product_names, prices, links))

        with open('../Price Lists/Monitors.csv', "w", newline='') as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in products:
                writer.writerow(item)
        print("=====Writing to file complete=====\n")

    def keyboards(self):
        driver = self.driver
        driver.get('https://www.evetech.co.za/components/buy-cheapest-gaming-keyboard-in-south-africa-52.aspx')

        print('Running Evetech in headless mode')

        product_names = [name.text for name in driver.find_elements_by_class_name('myProductName')]
        prices = [price.text for price in driver.find_elements_by_class_name('price')]
        links = [link.get_attribute('href') for link in driver.find_elements_by_link_text('More Info')]
        print(f'Found {len(product_names)} Keyboard Products')
        print("Finished Evetech Keyboards Collection")
        print('Now writing to file')

        products = sorted(zip(product_names, prices, links))

        with open('../Price Lists/Keyboards.csv', "w", newline='') as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in products:
                writer.writerow(item)
        print("=====Writing to file complete=====\n")

    def mice(self):
        driver = self.driver
        driver.get('https://www.evetech.co.za/components/gaming-mouse-117.aspx')

        print('Running Evetech in headless mode')

        product_names = [name.text for name in driver.find_elements_by_class_name('myProductName')]
        prices = [price.text for price in driver.find_elements_by_class_name('price')]
        links = [link.get_attribute('href') for link in driver.find_elements_by_link_text('More Info')]
        print(f'Found {len(product_names)} Mouse Products')
        print("Finished Evetech Mouse Collection")
        print('Now writing to file')

        products = sorted(zip(product_names, prices, links))

        with open('../Price Lists/Mouses.csv', "w", newline='') as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in products:
                writer.writerow(item)
        print("=====Writing to file complete=====\n")

    def cpu(self):
        driver = self.driver
        driver.get('https://www.evetech.co.za/components/buy-cpu-processors-online-164.aspx')

        print('Running Evetech in headless mode')

        product_names = [name.text for name in driver.find_elements_by_class_name('myProductName')]
        prices = [price.text for price in driver.find_elements_by_class_name('price')]
        links = [link.get_attribute('href') for link in driver.find_elements_by_link_text('More Info')]
        print(f'Found {len(product_names)} CPU Products')
        print("Finished Evetech CPU Collection")
        print('Now writing to file')

        products = sorted(zip(product_names, prices, links))

        with open('../Price Lists/CPU.csv', "w", newline='') as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in products:
                writer.writerow(item)
        print("=====Writing to file complete=====\n")