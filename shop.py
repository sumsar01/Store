import numpy as np
import datetime as dt


class Shop:
    pass

class Book:
    """ """
    def __init__(self):
        self.reciepts = [] # list of reciepts 
        self.day_sales = []   # list of sales for each day
        self.day_costs = []  # list of variable costs for each day
        self.day_balance = []    # list of sales - variable cost for each day


    def add_reciepts(self, reciepts):
        pass

    def find_day_costs(self, date):
        day_costs = 0 
        reciepts_of_day_costs = list(filter(lambda e: e[0].date() == date and e[2] < 0, self.reciepts))
        for i in range(len(reciepts_of_day_costs)):
            day_costs += reciepts_of_day_costs[i][2] 
        self.day_costs.append(day_costs)

    def find_day_sales(self, date):
        day_sales = 0 
        reciepts_of_day_sales = list(filter(lambda e: e[0].date() == date and e[2] > 0, self.reciepts))
        for i in range(len(reciepts_of_day_sales)):
            day_sales += reciepts_of_day_sales[i][2] 
        self.day_sales.append(day_sales)

    def print_history(self):
        unique_days_in_reciepts = np.unique([e[0].date() for e in self.reciepts])
        print("{:<10} {:<10} {:<10}".format("Sales", "Costs", "Date"))
        for i in range(len(self.day_sales)):
            print("{:<10} {:<10} {:<10}".format(self.day_sales[i], self.day_costs[i], unique_days_in_reciepts[i]))

class Account:
    """
    An account of the current monetary holdings.
    Must be initialized with current holdings.

    Account(starting_holdings)

    Methods:

    add_transaction(sum)
    take a number and add it to holdings. 
    The number can be negative to describe 
    spent money.

    get()
    Will return current holdings in the account.
    """
    def __init__(self, starting_holdings):
        if type(float(starting_holdings)) == float():
            self.account_holding = float(starting_holdings)
        else:
            ValueError("Error: Starting holdings must be a float or int...")

    def add_transaction(self, sum):
        if type(float(sum)) == float():
            self.account_holding += float(sum)
        else:
            ValueError("Error: sum must be a float or int...")

    def get(self):
        return self.account_holding

class Sale:
    """
    Make a sale of either a list of IDs or a single ID
    must take the used item stock, the book for reciepts 
    and the account used for the transaction.

    Sale(ID, amount, stock, book, account)

    ID - Is either a single ID or a list of IDs on the form [ID_1, ID_2, ...].
    amount - Is the amount of items bought of ID, either a single int or a list [amount_1, amount_2, ...].
    stck - The stock used in the transaction.
    book - The book used for the transaction.
    account - the account used for the transaction.
    """
    
    def __init__(self, ID, amount, stock, book, account):
        self.sum = 0
        receipt_list = []
        if type(ID) == list:
            for i in range(len(ID)):
                stock.use_item(ID[i], amount[i])
                price = stock.get_price(ID[i])
                self.sum += amount[i]*price[i]
                receipt_list.append((ID[i], amount[i]))
            else: 
                stock.use_item(ID, amount)
                price = stock.get_price(ID)
                self.sum += amount*price
                receipt_list.append((ID, amount))

        receipt = Receipt(receipt_list, stock)
        book.add_reciepts(self, reciepts)
        account.add_transaction(sum)

        print("".format("Item", "Amount", "Price pr. unit"))
        if type(ID) == list:
            for i in range(len(ID)):
                print("{:<20} {:<5} {:<5}".format(stock.get_item(ID[i]), amount[i], stock.get_price(ID[i])))
        else:
            print("{:<20} {:<5} {:<5}".format(stock.get_item(ID), amount, stock.get_price(ID)))

        print("\n")
        print("Total: {} kr".format(sum))

class Purchase:
    """
    Make a pruchase of either a list of IDs or a single ID 
    and a given amount of that item eithher in list form or as a single int.
    Must take the used item stock, the book for reciepts 
    and the account used for the transaction.

    Sale(ID, amount, stock, book, account)

    ID - Is either a single ID or a list of IDs on the form [ID_1, ID_2, ...].
    amount - Is the amount of items bought of ID, either a single int or a list [amount_1, amount_2, ...].
    stck - The stock used in the transaction.
    book - The book used for the transaction.
    account - the account used for the transaction.
    """
    def __init__(self, ID, amount, stock, book, account):
        self.sum = 0
        receipt_list = []
        if type(ID) == list:
            for i in range(len(ID)):
                stock.use_item(ID[i], amount[i])
                price = stock.get_cost(ID[i])
                self.sum += amount[i]*price[i]
                receipt_list.append((ID[i], amount[i]))
            else: 
                stock.use_item(ID, amount)
                price = stock.get_cost(ID)
                self.sum += amount*price
                receipt_list.append((ID, amount))

        receipt = Receipt(receipt_list, stock, "p")
        book.add_reciepts(self, reciepts)
        account.add_transaction(-sum) #romving used amount

        print("".format("Item", "Amount", "Price pr. unit"))
        if type(ID) == list:
            for i in range(len(ID)):
                print("{:<20} {:<5} {:<5}".format(stock.get_item(ID[i]), amount[i], stock.cost(ID[i])))
        else:
            print("{:<20} {:<5} {:<5}".format(stock.get_item(ID), amount, stock.get_cost(ID)))

        print("\n")
        print("Total: {} kr".format(sum))

class Counter:
    pass

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

    get_price(ID)
        Returns price of selling on item with ID.

    get_cost(ID)
        Get the cost of buying home on unit of the item with ID.

    get_item(ID)
        returns stock item with ID.
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

    def get_price(self, ID):
        return self.stock[ID][1]

    def get_cost(self, ID):
        return self.stock[ID][0].cost

    def get_item(self, ID):
        return self.stock[ID]

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
            raise ValueError("Error: wrong type the description must be a string...")


    def set_cost(self, new_cost):
        if type(new_cost) == float:
            self.cost = new_cost
        else:
            raise ValueError("Error: wrong type the new cost must be a float...")

class Clerk:
    pass

class Receipt:
    pass
