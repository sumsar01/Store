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
        [],

    "employees":
        ["Michael", "Rasmus"]
    }


def supply(shop):
    done = False
    while not done:
        print(supply_options)
        option = input("Chose an option: ")
        if option == "1":
            print("Adding new sales item...")
            item_ID = input("Item ID: ")
            item_name = input("Item name: ")
            item_price = float(input("Item price: "))
            item_unit = input("What is the unit of the item?: ")
            item = {item_ID: [item_name, item_price, item_unit, 0]}
            shop["inventory"].extend(item)

        if option == "2":
            pass

        if option == "3":
            pass

        if option == "4":
            pass

        if option == "0":
            pass
    #tilføj varer
    #fjern varer
    #se lager
    #opdater lager
    #betal for lager
    #købsnota


supply(shop)



