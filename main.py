from evetech import Evetech
from wootware import Wootware


print("PLEASE DONT CLOSE THIS WINDOW")
print("FETCHING UPDATED PRODUCTS AND PRICES\n")
evetech = Evetech()
wootware = Wootware()

evetech.ssd()
evetech.graphics_cards()

wootware.ssd()
wootware.graphics_cards()

print('\nCompleted you can now Close this window')
print('and check the folder for updated price lists')


