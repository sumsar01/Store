
def open_shop(shop):
    """Denne funktion optæller kassen, varebeholdningen og udskriver disse. 
    Til sidst laves en ny bon."""

    #optæl kasse
    print(f"Kassen har {shop['cash']} penge")
    #optæl varebeholdning
    print("Varelageret indeholder:\n")
    for key in shop["inventory"]:
        print(f"Vare: {shop['inventory'][key][0]}    Mængde: {shop['inventory'][key][3]}")
    #ny bong
    print("Making a new and empty receipt for the day.")
    shop["receipts"].clear()
