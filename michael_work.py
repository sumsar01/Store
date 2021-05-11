import numpy as np
import datetime as dt
import shop
    
class Reciept:
    """ This class is used to hold the reciept of transactions.

        Arguments: 
        list_of_id_quantity {[(ID, quantity),...]} -- To make a reciept object one has to supply a list of tuples: (ID, quantity)
        which contains the ID of the product bought and the quantity.

        stock {Stock()} -- A stock object has to be supplied to be able to fetch the price/cost of each entry
        on a given reciept.

        Keyword arguments:
        purchase sale {string} -- A string that must be either "s" if the reciept is for a sale by the shop or "p" if
        it is for a purchase buy the shop from a supplier.

        Returns:
        Reciept object. The object has a date, item_entries which contains a list of tuples: (ID, quantity, total price/cost for this ID),
        a total price/cost and finally whether it was a purchase or sale.
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


    def print_reciept(self):
        print("\n\t   RECIEPT \t")
        print("{:<10} {:<10} {:<10}".format("ID", "Amount", "Price"))
        for item in self.item_entries:
            ID = item[0]
            amount = item[1]
            price = item[2]
            print("{:<10} {:<10} {:<10}".format(ID, amount, price))
        print("Total:\t\t       {:<30}\n".format(self.total))





