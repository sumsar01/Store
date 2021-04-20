from datetime import date
import json
shop = {
    "inventory": 
        {
        123: ["Kartofler", 4.75, "kg", 100],
        143: ["Makrelguf", 10.50, "pakke", 30],
        185: ["Fintmalet kaffe", 44.25, "stk", 40]
        },

    "cash" : 
        588.75,

    "receipts": 
        [(123, 50), (143, 20), (123, 30)],

    "employees":
        ["Michael", "Rasmus"]
    }

def close_shop(shop):
    cash = shop["cash"]
    receipts = shop["receipts"]
    inventory = shop["inventory"]
    #print dag
    print(f"Date: {date.today()}")
    #optæl kasse
    print(f"Register contains {shop['cash']} money")
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

    #afstæm kasse
    ##find overskud
    #udskriv kasse raport
    pass

close_shop(shop)