from venv.product_search import ProductSearch

evetech = ProductSearch()
evetech_ssd = evetech.eve_search("https://www.evetech.co.za/PC-Components/buy-solid-state-drives-83.aspx")

print(evetech_ssd)