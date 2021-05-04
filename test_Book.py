import unittest
import shop
import numpy as np


class TestBook(unittest.TestCase):

    def setUp(self):
        self.test_book = shop.Book("testBook")
        test_stock = shop.Stock()
        n = 10
        self.test_receipts = []
        for i in range(n):
            receipt_len = np.random.randint(50)
            rnd_list1 = np.random.randint(500, size=receipt_len)
            rnd_list2 = np.random.randint(10, size=receipt_len)
            self.test_receipts.append(shop.Receipt(list(zip(rnd_list1, rnd_list2)), test_stock, receipt_len))
            print()
            
    def test_add_receipt(self):
        test_receipt = self.test_receipts[0]
        self.test_book.add_receipt(test_receipt)

        self.assertEqual(test_receipt, self.test_book.day_receipts[0])

    def test_2(self):
        pass

    def test_3(self):
        pass


if __name__ == '__main__':
    unittest.main()