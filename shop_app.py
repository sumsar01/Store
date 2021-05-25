import shop as sp
import pickle
import os
from storage import *



options = """
    Store options:
    1) Sell items
    2) Update supply

    0) Save & Exit
    """

save_dir = os.getcwd()
filename = "shop1"
if os.path.isfile(save_dir + filename + '.p'):
    shop = load_data(save_dir, filename)
else:
    shop = sp.Shop(filename, 100000)

done = True
while done == True:
    print(options)
    opt = input("Pick an option: ")
    if opt == "0":
        shop.save_shop()
        save_data(shop, save_dir, filename)
        done = False
        print("The shop is closed...")

    elif opt == "1":
        shop.sell_items()

    elif opt == "2":
        shop.update_supply()

    else:
        print("Error: unkown option try again...")