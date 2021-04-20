def open_shop(shop):
    #optæl kasse
    #optæl varebeholdning
    #ny bong
    pass

def close_shop(shop):
    #optæl kasse
    #optæl bonner
    #bestil nye varer
    #afstæm kasse
    #udskriv kasse raport
    pass

def sale():
    #for alle varer i salget:
    ##fjern vare fra lager
    ##læg priser til sum
    ##opdater bonner
    #udskriv bon
    #modtag betaling til kassen
    #fejl beskeder for varer som ikke findes
    pass

supply_options = """
    Supply options:
    1) Add item
    2) Remove item
    3) View supply
    4) Update supply

    0) Exit
                """

def supply(shop):
    """Enters supply options.
    1) Allows user to add item to inventory under item IDs
    2) Allows user to remove items using item IDs
    3) Show user current item stock
    4) Allows user to restock items by using their ID and number of added items


    """

    done = False
    while not done:
        print(supply_options)
        option = input("Chose an option: ")

        # Add item
        if option == "1":
            print("Adding new sales item...")
            item_ID = input("Item ID: ")
            if item_ID in shop["inventory"]:
                print("Error: ID already exist in inventory...")
            else:
                item_name = input("Item name: ")
                item_price = float(input("Item price: "))
                item_unit = input("What is the unit of the item?: ")
                item = {item_ID: [item_name, item_price, item_unit, 0]}
                shop["inventory"].update(item)

        # Remove item
        if option == "2":
            print("Removing item from stock...")
            item_ID = input("Item ID: ")
            if item_ID in shop["inventory"]:
                del shop["inventory"][item_ID]
            else:
                print("Error: Item ID not found...")

        # View supply
        if option == "3":
            print("{:10}{:20}{:7}{:10}{:10}".format("Item ID", "Name", "Price", "Units", "Stock"))
            for item in shop["inventory"]:
                print("{:7}   {:20}{:5}  {:5} {:7}".format(item, shop["inventory"][item][0], shop["inventory"][item][1], shop["inventory"][item][2], shop["inventory"][item][3]))

        # Update supply
        if option == "4":
            print("Updation store...")
            item_ID = int(input("Item ID: "))
            if item_ID not in shop["inventory"]:
                print("Error: Item ID not found...")
            else:
                print(f'{item_ID} is {shop["inventory"][item_ID][0]} currently supply {shop["inventory"][item_ID][3]} in stock...')
                updated_stock = int(input("How many would you like to add?: "))
                shop["inventory"][item_ID][3] += updated_stock
                print(f'{item_ID} is {shop["inventory"][item_ID][0]} updated supply {shop["inventory"][item_ID][3]} in stock...')

        # Exit supply
        if option == "0":
            print("Exiting supply options...")
            done = True



