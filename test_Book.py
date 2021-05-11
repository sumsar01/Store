import unittest
import shop
import numpy as np


class TestBook(unittest.TestCase):

    def setUp(self):
        self.test_book = shop.Book("testBook")
        test_stock = shop.Stock()
        n = 10
        self.test_sale_receipts = []
        self.test_purc_receipts = []
        for _ in range(n):
            receipt_len = np.random.randint(50)
            rnd_list1 = np.random.randint(500, size=receipt_len)
            rnd_list2 = np.random.randint(10, size=receipt_len)
            list_tup = list(zip(rnd_list1, rnd_list2))
            self.test_sale_receipts.append(shop.Receipt(list_tup, test_stock))
            self.test_purc_receipts.append(shop.Receipt(list_tup, test_stock, "p"))
            
    def test_add_receipt(self):
        test_receipt1 = self.test_sale_receipts[0]
        test_receipt2 = self.test_sale_receipts[0]
        self.test_book.add_receipt(test_receipt1)
        self.test_book.add_receipt(test_receipt2)

        
        self.assertEqual(test_receipt1, self.test_book.day_receipts[0])
        self.assertEqual(test_receipt2, self.test_book.day_receipts[1])

    def test_find_day_costs(self):
        receipt1 = self.test_purc_receipts[0]
        receipt2 = self.test_purc_receipts[1]
        self.test_book.add_receipt(receipt1)
        self.test_book.add_receipt(receipt2)
        self.test_book.find_day_costs()
        if(receipt1.purchase_sale == "p" and receipt2.purchase_sale == "p"):
            self.assertEqual(self.test_book.day_costs, receipt1.total + receipt2.total)



    def test_find_day_sales(self):
        pass

    def test_store_balance(self):
        pass

    def test_todays_receipts(self):
        pass


if __name__ == '__main__':
    unittest.main()