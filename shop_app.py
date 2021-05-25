import shop as sp
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
        sale_options = """
    Sale options:

    1) Sell single item
    2) Sell more items

    0) Exist sale
            """
        print(sale_options)
        choice = input("Pick an option: ")
        if choice == "0":
            pass
        elif choice == "1":
            ID = input("Input item ID: ")
            amount = int(input("Input the amount of that item you want to buy: "))
            shop.sell_items(ID, amount)
        elif choice == "2":
            ID = []
            amount = []
            num = int(input("How many different items are you buying? "))
            for i in range(0,num):
                ID.append(input("Input ID of " + str(i+1) + "th item: "))
                amount.append(int(input("Input amount of " + str(i+1) + "th item: ")))
            shop.sell_items(ID, amount)
        else:
            print("Error: Not a valid choice...")

    elif opt == "2":
        restock_options = """
    Restock options:

    1) restock single item
    2) restock more items

    0) Exist sale
            """
        print(restock_options)
        choice = input("Pick an option: ")
        if choice == "0":
            pass
        elif choice == "1":
            ID = input("Input item ID: ")
            amount = int(input("Input the amount of that item you want to buy: "))
            shop.update_supply(ID, amount)
        elif choice == "2":
            ID = []
            amount = []
            num = int(input("How many different items are you buying? "))
            for i in range(0,num):
                ID.append(input("Input ID of " + str(i+1) + "th item: "))
                amount.append(int(input("Input amount of " + str(i+1) + "th item: ")))
            shop.update_supply(ID, amount)
        else:
            print("Error: Not a valid choice...")
    else:
        print("Error: unkown option try again...")