import numpy as np
import datetime as dt
import csv

class Shop:
    pass

class Book:
    """ This class is made for bookkeeping. This bookkeeping is contained in two databases - one in memory and one in a csv file.
        The database in memory holds the receipts of the current day. When the day ends these receipts are counted to find the
        total sales, costs, and balance during the day. These informations are stored in the balance_history csv file. The receipts 
        of the day are also stored in a separate csv file containing receipts from previous days also.

        Arguments:
        dbname -- The prefix name that is used to generate the two csv databases (one for receipts and one for balance history).

        Methods:
        add_receipt() -- adds a new receipt to the list of receipts for the day

        daily_close() -- This method writes receipts and (sales, costs, balance) to their respective files and reinitializes
        important book fields, so they are clean for the next bookkeeping day.

        print_balance_history() -- Prints the balance history - rows of (Date, sales, costs, balance)
    """
    def __init__(self, dbname):
        self.dbname = dbname
        self.day_receipts = []
        self.day_sales = 0 
        self.day_costs = 0
        self.day_balance = 0
        db_receipts = open(f"{dbname}" + "_receipts.csv", "x")
        db_balance_history = open(f"{dbname}" + "_balance_history.csv", "x")
        db_receipts.close()
        db_balance_history.close()

    def add_receipt(self, receipt):
        self.day_receipts.append(receipt)

    def daily_close(self):
        self.find_day_sales()
        self.find_day_costs()
        self.store_balance()
        self.store_todays_receipts()

    def find_day_costs(self):
        receipts_purchases = list(filter(lambda receipt: receipt.purchase_sale == "p", self.day_receipts))
        self.day_costs = 0
        for i in range(len(receipts_purchases)):
            self.day_costs += receipts_purchases[i].total 

    def find_day_sales(self):
        receipts_sales = list(filter(lambda receipt: receipt.purchase_sale == "s", self.day_receipts))
        self.day_sales = 0
        for i in range(len(receipts_sales)):
            self.day_sales += receipts_sales[i].total 

    def store_balance(self):
        with open(f"{self.dbname}" + "_balance_history.csv", "w", newline="") as file:
            date = dt.datetime.today()
            writer = csv.writer(file, delimiter=" ")
            writer.writerow([date, self.day_sales, self.day_costs, self.day_balance])
        self.day_sales = 0 
        self.day_costs = 0 
        self.day_balance = 0

    def store_todays_receipts(self):
        with open(f"{self.dbname}" + "_receipts.csv", "w", newline="") as file:
            for receipt in self.day_receipts:
                date = dt.datetime.today()
                writer = csv.writer(file, delimiter=" ")
                writer.writerow([date, receipt.total, receipt.purchase_sale, receipt.item_entries])
        self.day_receipts = [] 

    def print_balance_history(self):
        print("{:<10} {:<10} {:<10} {:<10}".format("Date", "Sales", "Costs", "Balance"))
        with open(f"{self.dbname}" + "_balance_history.csv", "r", newline="") as file:
            reader = csv.reader(file, delimiter=" ")
            for row in reader:
                print("{:<10} {:<10} {:<10} {:<10}".format(row[0], row[1], row[2], row[3]))

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
    must take the used item stock, the book for receipts 
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
                self.sum += amount[i]*price
                receipt_list.append((ID[i], amount[i]))
        else: 
            stock.use_item(ID, amount)
            price = stock.get_price(ID)
            self.sum += amount*price
            receipt_list.append((ID, amount))

        receipt = Receipt(receipt_list, stock)
        book.add_receipt(receipt)
        account.add_transaction(self.sum)

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
    Must take the used item stock, the book for receipts 
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
                self.sum += amount[i]*price
                receipt_list.append((ID[i], amount[i]))
        else: 
            stock.update_stock(ID, amount)
            price = stock.get_cost(ID)
            self.sum += amount*price
            receipt_list.append((ID, amount))

        receipt = Receipt(receipt_list, stock, "p")
        book.add_receipt(receipt)
        account.add_transaction(-self.sum) #romving used amount

        print("".format("Item", "Amount", "Price pr. unit"))
        if type(ID) == list:
            for i in range(len(ID)):
                print("{:<20} {:<5} {:<5}".format(stock.get_item(ID[i]).name, amount[i], stock.get_cost(ID[i])))
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
