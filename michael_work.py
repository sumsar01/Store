import numpy as np
import datetime as dt
    
class Book:
    """ """
    def __init__(self):
        self.reciepts = [] # list of reciepts 
        self.day_sales = []   # list of sales for each day
        self.day_costs = []  # list of variable costs for each day
        self.day_balance = []    # list of sales - variable cost for each day


    def add_reciepts(self, file):
        pass

    def find_total_in(self, reciepts, date):
        pass

    def find_day_sales(self, day):
        day_sales = 0 
        reciepts_of_day_sales = list(filter(lambda e: e[0].date.day == day and e[2] > 0, self.reciepts))
        for i in range(len(reciepts_of_day_sales)):
            day_sales += reciepts_of_day_sales[2] 
        self.day_sales.append(day_sales)

    def print_history(self):
        unique_days_in_reciepts = np.unique([e[0].date.day for e in self.reciepts])
        print("{:<10} {:<10} {:<10}".format("Sales", "Costs", "Date"))
        for i in range(len(self.day_sales)):
            print("{:<10} {:<10} {:<10}".format(self.day_sales[i], self.day_costs[i], unique_days_in_reciepts[i]))

book = Book()
book.reciepts = [(dt.datetime.now(), [[1, 10, 40, 50], [2, 10, 30, 50], [3, 40, 10, 20]], 20), (dt.datetime.now(), [[1, 10, 40, 50], [2, 10, 30, 50], [3, 40, 10, 20]], 20)]
book.find_day_sales(dt.datetime.now().day)


#book.day_sales = [10, 20]
#book.day_costs = [10, 20]
#book.day_balance = [0, 0]

#book.print_history()
