class Shop:

class Book:

class Account:

class Transaction:

class Counter:

class Stock:
    """
    Contains a dict of all item in stock


    Methods:

    add_item(ID, StockUnit, price, amount_in_stock)
        Takes an ID str, a StockUnit object, a price and the amount of items in stock
        and store them in the stock.

    use_item(ID, amount)
        Used when units of items are removed from the stock. 
        Takes an ID str and the amount of items removed.

    update_stock(ID, amount)
        Used for updating supply in the stock.
        Takes an ID str and the amount of items added to the stock.

    delete_item(ID)
        Delete an item from the stock dict with the given ID string.

    stock_information()
        Prints informations on the items in the stock.
    """
    def __init__(self):
        self.stock = {}

    def add_item(self, ID, StockUnit, price, amount_in_stock):
        if ID in self.stock:
            print("Error: ID already in stock...")
        else:
            holder = {ID : [StockUnit, price, amount_in_stock]}
            self.stock.update(holder)

    def use_item(self, ID, amount):
        if ID in self.stock:
            self.stock[ID][2] -= amount
        else:
            print("Error: ID not found...")

    def update_stock(self, ID, amount):
        if ID in self.stock:
            self.stock[ID][2] += amount
        else:
            print("Error: ID not found...")

    def delete_item(self, ID):
        if ID in self.stock:
            del self.stock[ID]
        else:
            print("Error: ID not found...")

    def stock_information(self):
        print("{:<5} {:<20} {:<10} {:<10} {:<10} {:<10}".format("ID", "Name", "Unit", "Cost", "Price", "Amount"))
        for ID in self.stock:
            print("{:<5} {:<20} {:<10} {:<10} {:<10} {:<10}".format(ID, self.stock[ID][0].name, self.stock[ID][0].unit, self.stock[ID][0].cost, self.stock[ID][1], self.stock[ID][2]))
        print("\n")


class StockUnit:
    """
    Stock item.

    StockUnit(name, cost, unit, description = "")
    name - name of item
    cost - cost of buying item home to the shop
    unit - the unit of the item
    description - a short description of the item


    Methods:

    get_information(verbose = False)
        prints the information on the item.
        if verbose is True more information is given.

    set_description(new_description)
        set a new description of the item.

    set_cost(new_cost)
        set a new cost of the item.

    """
    
    def __init__(self, name, cost, unit, description = ""):
        self.name = name
        self.cost = cost
        self.unit = unit
        self.description = description

    def get_information(self, verbose = False):
        if verbose == True:
            print("{:<20} {:<10} {:<10}".format("Name", "Cost", "Unit"))
            print("{:<20} {:<10} {:<10}".format(self.name, self.cost, self.unit))
            print("\nDescription:")
            print("\t",self.description)
        else:
            print("{:<20} {:<10} {:<10}".format(self.name, self.cost, self.unit))

    def set_description(self, new_description):
        if type(new_description) == str:
            self.description = new_description
        else:
            print("Error: wrong type the description must be a string...")


    def set_cost(self, new_cost):
        if type(new_cost) == float:
            self.cost = new_cost
        else:
            print("Error: wrong type the new cost must be a float...")


class Clerk:

class Receipt:

