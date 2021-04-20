from store_function import *

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



supply(shop)
