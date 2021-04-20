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
        [1, 2, 3, 4],

    "employees":
        ["Michael", "Rasmus"]
    }

def open_shop(shop):

    #optæl kasse
    print(f"Kassen har {shop['cash']} penge")
    #optæl varebeholdning
    print("Varelageret indeholder:\n")
    for key in shop["inventory"]:
        print(f"Vare: {shop['inventory'][key][0]}    Mængde: {shop['inventory'][key][3]}")
    #ny bong
    print("Making a new and empty receipt for the day.")
    shop["receipts"].clear()

print(shop["receipts"])
open_shop(shop)
print(shop["receipts"])