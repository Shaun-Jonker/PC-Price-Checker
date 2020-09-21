from modules.product_search import ProductSearch
from modules.writer import Writer

writer = Writer()

#evetech = ProductSearch()
#wootware = ProductSearch()
foxytech = ProductSearch()

# evetech_ssd = evetech.eve_search("https://www.evetech.co.za/PC-Components/buy-solid-state-drives-83.aspx", "Solid State Drives")
# writer.write_to_file("Solid State Drives", evetech_ssd)

# wootware_ssd = wootware.woot_search("https://www.wootware.co.za/computer-hardware/hard-drives-ssds/solid-state-disks"
                                   # "/shopby/in_stock_with_wootware?limit=500", "Solid State Drives")
# writer.append("Solid State Drives", wootware_ssd)

#evetech_graphics_cards = evetech.eve_search("https://www.evetech.co.za/components/nvidia-ati-graphics-cards-21.aspx", "Graphics Cards")


foxytech_ssd = foxytech.foxy_search("https://www.foxytech.co.za/product-category/hardware/storage/solid-state-drives-ssd/?orderby=by_stock", "Solid State Drives")
writer.write_to_file("Solid State Drives", foxytech_ssd)