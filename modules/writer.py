import csv


class Writer:

    def write_to_file(self, file, product_list):

        with open(f'Price Lists/{file}.csv', "w", newline='', encoding="utf-8") as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in product_list:
                writer.writerow(item)
        print("=====Writing to file complete=====\n")

    def append (self, file, product_list):

        with open(f'Price Lists/{file}.csv', "a+", newline='', encoding="utf-8") as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in product_list:
                writer.writerow(item)
        print("=====Writing to file complete=====\n")

