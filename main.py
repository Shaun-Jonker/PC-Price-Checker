from modules.product_search import ProductSearch
from modules.writer import Writer


print("PLEASE DONT CLOSE THIS WINDOW")
print("FETCHING UPDATED PRODUCTS AND PRICES\n")

writer = Writer()

evetech = ProductSearch()
wootware = ProductSearch()
foxytech = ProductSearch()


# Solid State Drive Web Data
evetech_ssd = evetech.eve_search("https://www.evetech.co.za/PC-Components/buy-solid-state-drives-83.aspx", "Solid State Drives")
wootware_ssd = wootware.woot_search("https://www.wootware.co.za/computer-hardware/hard-drives-ssds/solid-state-disks"
                                    "/shopby/in_stock_with_wootware?limit=500", "Solid State Drives")
foxytech_ssd = foxytech.foxy_search("https://www.foxytech.co.za/product-category/hardware/storage/solid-state-drives"
                                    "-ssd/?orderby=by_stock", "Solid State Drives")


# Write Solid State Drive data to File
writer.write_to_file("Solid State Drives", evetech_ssd)
writer.append("Solid State Drives", wootware_ssd)
writer.append("Solid State Drives", foxytech_ssd)


# Graphics Card Web Data
evetech_graphics_cards = evetech.eve_search("https://www.evetech.co.za/components/nvidia-ati-graphics-cards-21.aspx", "Graphics Cards")
wootware_graphics_cards = wootware.woot_search('https://www.wootware.co.za/computer-hardware/video-cards-video-devices/shopby/in_stock_with_wootware', 'Graphics Cards')
foxytech_graphics_cards = foxytech.foxy_search('https://www.foxytech.co.za/product-category/hardware/computer-components/graphics-card/?orderby=by_stock', 'Graphics Cards')


# Write Graphics Cards data to File
writer.write_to_file("Graphics Cards", evetech_graphics_cards)
writer.append('Graphics Cards', wootware_graphics_cards)
writer.append('Graphics Cards', foxytech_graphics_cards)


# Monitor Web Data
evetech_Monitors = evetech.eve_search("https://www.evetech.co.za/PC-Components/pc-monitors-89.aspx", "Monitors")
wootware_Monitors = wootware.woot_search('https://www.wootware.co.za/computer-hardware/lcds-monitors/shopby/in_stock_with_wootware', 'Monitors')
foxytech_Monitors = foxytech.foxy_search('https://www.foxytech.co.za/product-category/peripherals/monitors/?orderby=by_stock', 'Monitors')


# Write Monitor data to File
writer.write_to_file("Monitors", evetech_Monitors)
writer.append('Monitors', wootware_Monitors)
writer.append('Monitors', foxytech_Monitors)


# CPU Web Data
evetech_cpu = evetech.eve_search('https://www.evetech.co.za/components/buy-cpu-processors-online-164.aspx', "CPU")
wootware_cpu = wootware.woot_search('https://www.wootware.co.za/computer-hardware/cpus-processors/shopby/in_stock_with_wootware', 'CPU')
foxytech_cpu = foxytech.foxy_search("https://www.foxytech.co.za/product-category/hardware/computer-components/cpu-processors/?orderby=by_stock", "CPU")

print('\nCompleted you can now Close this window')
print('and check the folder for updated price lists')