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
        self.account_holding = 0
        try:
            self.account_holding = float(starting_holdings)
        except:
            raise TypeError("sum must be a number...")

    def add_transaction(self, sum):
        try:
            self.account_holding += float(sum)
        except:
            raise TypeError("sum must be a number...")

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
        book.add_reciepts(self, receipt)
        account.add_transaction(sum)

        print("".format("Item", "Amount", "Price pr. unit"))
        if type(ID) == list:
            for i in range(len(ID)):
                print("{:<20} {:<5} {:<5}".format(stock.get_item(ID[i]).name, amount[i], stock.get_price(ID[i])))
        else:
            print("{:<20} {:<5} {:<5}".format(stock.get_item(ID).name, amount, stock.get_price(ID)))

        print("\n")
        print("Total: {} kr".format(self.sum))

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
                stock.update_stock(ID[i], amount[i])
                price = stock.get_cost(ID[i])
                self.sum += amount[i]*price[i]
                receipt_list.append((ID[i], amount[i]))
        else: 
            stock.update_stock(ID, amount)
            price = stock.get_cost(ID)
            self.sum += amount*price
            receipt_list.append((ID, amount))

        receipt = Receipt(receipt_list, stock, "p")
        book.add_reciepts(receipt)
        account.add_transaction(-self.sum) #romving used amount

        print("".format("Item", "Amount", "Price pr. unit"))
        if type(ID) == list:
            for i in range(len(ID)):
                print("{:<20} {:<5} {:<5}".format(stock.get_item(ID[i]).name, amount[i], stock.cost(ID[i])))
        else:
            print("{:<20} {:<5} {:<5}".format(stock.get_item(ID).name, amount, stock.get_cost(ID)))

        print("\n")
        print("Total: {} kr".format(self.sum))

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
            raise ValueError("Error: ID already in stock...")
        else:
            holder = {ID : [StockUnit, price, amount_in_stock]}
            self.stock.update(holder)

    def use_item(self, ID, amount):
        if ID in self.stock:
            try:
                self.stock[ID][2] -= amount
            except:
                raise TypeError("Wrong type the added amount must be a number...")
        else:
            raise ValueError("Error: ID not found...")

    def update_stock(self, ID, amount):
        if ID in self.stock:
            try:
                self.stock[ID][2] += amount
            except:
                raise TypeError("Wrong type the added amount must be a number...")
        else:
            raise ValueError("ID not found...")

    def delete_item(self, ID):
        if ID in self.stock:
            del self.stock[ID]
        else:
            raise ValueError("ID not found...")

    def stock_information(self):
        print("{:<5} {:<20} {:<10} {:<10} {:<10} {:<10}".format("ID", "Name", "Unit", "Cost", "Price", "Amount"))
        for ID in self.stock:
            print("{:<5} {:<20} {:<10} {:<10} {:<10} {:<10}".format(ID, self.stock[ID][0].name, self.stock[ID][0].unit, self.stock[ID][0].cost, self.stock[ID][1], self.stock[ID][2]))
        print("\n")

    def get_price(self, ID):
        if ID in self.stock:
            return self.stock[ID][1]
        else:
            raise ValueError("ID not found...")

    def get_cost(self, ID):
        if ID in self.stock:
            return self.stock[ID][0].cost
        else:
            raise ValueError("ID not found...")

    def get_item(self, ID):
        if ID in self.stock:
            return self.stock[ID][0]
        else:
            raise ValueError("ID not found...")

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
            raise TypeError("Wrong type the description must be a string...")


    def set_cost(self, new_cost):
        if type(new_cost) == float:
            self.cost = new_cost
        else:
            raise TypeError("Wrong type the new cost must be a float...")

class Clerk:
    pass

class Receipt:
    """ This class is used to hold the receipt of transactions.

        Fields:
        date -- The date the receipt object was made.
        item_entries -- contains a list of tuples: (ID, quantity, total price/cost for this ID)
        total -- total price/cost of all receipt entries.
        purchase_sale -- "s" if the receipt is for a sale and "p" if purchase

        Arguments: 
        list_of_id_quantity {[(ID, quantity),...]} -- To make a receipt object one has to supply a list of tuples: (ID, quantity)
        which contains the ID of the product bought and the quantity.

        stock {Stock()} -- A stock object has to be supplied to be able to fetch the price/cost of each entry
        on a given receipt.

        Keyword arguments:
        purchase sale {string} -- A string that must be either "s" if the receipt is for a sale by the shop or "p" if
        it is for a purchase buy the shop from a supplier.

        Methods:
        calc_item_pricecost() -- For each entry on the receipt the total price/cost is calculated

        make_full_item_entries() -- populates the field item_entries.

        calc_total() -- populates the field total with the total price/cost
    """

    def __init__(self, list_of_id_quantity, stock, purchase_sale="s"):
        self.date = dt.datetime.now().date()
        self.item_entries = []
        self.total = 0
        self.purchase_sale = purchase_sale

        prices_or_costs = self.calc_item_pricecost(list_of_id_quantity, stock)
        self.item_entries = self.make_full_item_entries(list_of_id_quantity, prices_or_costs)
        self.calc_total()


    def calc_item_pricecost(self, list_of_id_q, stock):
        prices_costs = []
        for ID, quantity in list_of_id_q:
            price_cost = 0
            if self.purchase_sale == "s":
                price_cost = stock.get_price(ID)
            elif self.purchase_sale == "p":
                price_cost = stock.get_cost(ID)
            else:
                ValueError("purchase_sale need to be 's' or 'p'...")

            prices_costs.append(price_cost * quantity)
        return prices_costs
            
    def make_full_item_entries(self, list_of_id_quantity, prices_or_costs):
        item_entries_list = []
        for i in range(len(prices_or_costs)):
            id = list_of_id_quantity[i][0]
            quantity = list_of_id_quantity[i][1]
            item_entries_list.append((id, quantity, prices_or_costs[i]))
        return item_entries_list
    
    def calc_total(self):
        total = 0
        for i in range(len(self.item_entries)):
            total += self.item_entries[i][2]
        self.total = total 


    def print_receipt(self):
        print("\n\t   RECEIPT \t")
        print("{:<10} {:<10} {:<10}".format("ID", "Amount", "Price"))
        for item in self.item_entries:
            ID = item[0]
            amount = item[1]
            price = item[2]
            print("{:<10} {:<10} {:<10}".format(ID, amount, price))
        print("Total:\t\t       {:<30}\n".format(self.total))
