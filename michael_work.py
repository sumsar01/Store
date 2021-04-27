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
