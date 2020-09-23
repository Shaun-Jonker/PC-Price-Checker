from modules.product_search import ProductSearch
from modules.writer import Writer


writer = Writer()

titanice = ProductSearch()

titanice_graphics_cards = titanice.titan_search('https://www.titan-ice.co.za/hardware/gpus/', "Graphics Cards")
writer.append("Graphics Cards", titanice_graphics_cards)
