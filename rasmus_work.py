class Transaction:
    """
    """
    def __init__(self, ID, amount, stock, receipt):
        self.sum = 0

        for i in range(len(ID)):
            stock.use_item(ID[i], amount[i])
            price = stock.get_price(ID[i])
            self.sum += amount[i]*price[i]


array = [3, 5, 6, 7]

for i in range(len(array)):
    print(i)