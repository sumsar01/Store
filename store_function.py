from datetime import date
import json




def open_shop(shop):
    """This function counts the register, stash and prints these. Lastly, it makes a new receipt."""

    #optæl kasse
    print(f"Register contains {shop['cash']} money")
    #optæl varebeholdning
    print("Stash contains:\n")
    for key in shop["inventory"]:
        print(f"Item: {shop['inventory'][key][0]}    Amount: {shop['inventory'][key][3]}")
    #ny bong
    print("Making a new and empty receipt for the day.")
    shop["receipts"].clear()




########################
# Mangler dokumentation
########################
def close_shop(shop):
    cash = shop["cash"]
    receipts = shop["receipts"]
    inventory = shop["inventory"]
    #print dag
    print(f"Date: {date.today()}")
    #optæl kasse
    print(f"Register contains {cash} money")
    #optæl bon
    keys = shop["inventory"].keys()
    for key in keys:
        amount = 0
        for i in range(len(receipts)):
            if(key == receipts[i][0]):
                amount += receipts[i][1]
        print(f"Item: {inventory[key][0]}, Amount: {amount}")
    print("Items and the sold amount during the day:\n")
    #bestil nye varer
    done = False
    print("Order new supply...")
    

    order_list = []
    while not done:
        print("Order next item...")
        item_ID = input("Supply item ID: ")
        if item_ID == "":
            done = True
        else:
            item_ID = int(item_ID)
            if item_ID not in inventory:
                print("Item ID not found")
            else:
                order_amount = input("Enter order amount: ")
                order_list.append({item_ID : order_amount})
    order_file = open("order.json", "w")
    json.dump(order_list, order_file)
    order_file.close()




def sale(shop):
    """"
    Buying items untill an empty ID for an item is given.
    Count a bill for the customer and store items bought in a list
    prints a bill for the custormer
    adds the amount to "cash" in shop and the list of items to "receipts"
    """
    customer_bill = 0.0
    customer_receipt = []
    done = False

    while not done:
        print("Scanning next item... ")
        item_ID = input("Item ID: ")
        if item_ID == "":
            print("No more items pending...")
            break
        else:
            item_ID = int(item_ID)
            if item_ID not in shop["inventory"]:
                print("Error: Item ID not found...")
            else:
                item_number = int(input(f'How many {shop["inventory"][item_ID][0]} are you buying?: '))
                customer_receipt.append((item_ID, item_number))
                customer_bill += shop["inventory"][item_ID][1]*item_number
                shop["inventory"][item_ID][3] -= item_number
    shop["receipts"].extend(customer_receipt)
    shop["cash"] += customer_bill
    print("Printing bill...")
    for ID, amount in customer_receipt:
        print(f'{amount} {shop["inventory"][ID][0]}: {shop["inventory"][ID][1]*amount} kr')




def supply(shop):
    """
    Enters supply options.
    1) Allows user to add item to inventory under item IDs
    2) Allows user to remove items using item IDs
    3) Show user current item stock
    4) Allows user to restock items by using their ID and number of added items
    """

    supply_options = """
    Supply options:
    1) Add item
    2) Remove item
    3) View supply
    4) Update supply

    0) Exit
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



