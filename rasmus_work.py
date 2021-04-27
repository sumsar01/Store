class Transaction:
    """
    """
    def __init__(self, ID, amount, stock, account):
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

        receipt = Receipt(receipt_list)



receipt(ID, )

import datetime

dag = datetime.datetime.now()

print(dag.day)