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


help(sale)



"""
done = False
while not done:
    print("Velkommen til næste kunde...")
    sum = 0.0

    flere_varer = True
    while flere_varer:
        stregkode = input("indtast varer nr: ")
        if stregkode == "":
            flere_varer = False
        else:
            stregkode = int(stregkode)
            if stregkode in varelager:
                print("Varen er {} og prisen er {} kr, der er {} enheder på lager".format(varelager[stregkode][0], varelager[stregkode][1], varelager[stregkode][3]))
                antal = int(input("Hvor mange enheder købes? "))
                if antal == 0:
                    break
                varelager[stregkode][3] -= antal
                sum += int(varelager[stregkode][1])*antal
            else:
                print("Fejl stregkode findes ikke...")
            

    print("Det bliver {} kr".format(sum))
    svar = input("Er der flere kunder? y/n: ")
    if svar == 'n':
        done = True
        print("Der er ikke flere kunder...")
"""