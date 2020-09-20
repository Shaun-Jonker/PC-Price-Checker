from modules.product_search import ProductSearch

evetech = ProductSearch()
evetech_ssd = evetech.eve_search("https://www.evetech.co.za/PC-Components/buy-solid-state-drives-83.aspx")
evetech_graphics_cards = evetech.eve_search("https://www.evetech.co.za/components/nvidia-ati-graphics-cards-21.aspx")

print(evetech_ssd)
print(evetech_graphics_cards)

