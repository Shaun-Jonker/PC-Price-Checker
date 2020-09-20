from modules.evetech import Evetech
from modules.wootware import Wootware


print("PLEASE DONT CLOSE THIS WINDOW")
print("FETCHING UPDATED PRODUCTS AND PRICES\n")
evetech = Evetech()
wootware = Wootware()

evetech.ssd()
evetech.graphics_cards()
evetech.monitors()
evetech.keyboards()
evetech.mice()
evetech.cpu()

wootware.ssd()
wootware.graphics_cards()
wootware.monitors()
wootware.keyboards()
wootware.mice()
wootware.cpu()

print('\nCompleted you can now Close this window')
print('and check the folder for updated price lists')


