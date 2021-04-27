import numpy as np
import datetime as dt
    
class Reciept:
    def __init__(self, list_of_id_quantity, buy_sell="s"):
        self.date = dt.datetime.now().date()
        self.item_entries = []
        self.total = 0
        self.buy_sell = buy_sell

        prices_or_costs = calc_item_pricecost(list_of_id_quantity)
        self.item_entries = make_final_item_entries(list_of_id_quantity, prices_or_costs)
        calc_total()


    def calc_item_pricecost(self):
        if self.buy_sell == "s":
            # fetch prices of IDs (brug stock)
            # make list with all prices of IDs
            # multiply unit prices with quantities to get prices
            break
        if self.buy_sell == "b":
            # fetch costs of IDs (brug stock)
            # make list with costs of IDs
            # multiply unit costs with quantities to get costs
            break
        pass

            
    def make_full_item_entries():

        pass
    
    def calc_total():
        pass



        for ID, amount, 




book = Book()
book.reciepts = [(dt.datetime.now(), [[1, 10, 40, 50], [2, 10, 30, 50], [3, 40, 10, 20]], 20), (dt.datetime.now(), [[1, 10, 40, 50], [2, 10, 30, 50], [3, 40, 10, 20]], 20),
    (dt.datetime.now(), [[1, 30, 40, 0], [2, 20, 30, 0], [5, 40, 10, 0]], -30)]
book.find_day_sales(dt.datetime.now().date())
book.find_day_costs(dt.datetime.now().date())
print(book.day_costs)


#book.day_sales = [10, 20]
#book.day_costs = [10, 20]
#book.day_balance = [0, 0]

#book.print_history()
