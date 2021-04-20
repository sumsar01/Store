
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
