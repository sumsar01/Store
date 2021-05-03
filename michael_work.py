import numpy as np
import datetime as dt
    
class Reciept:
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
        return total
