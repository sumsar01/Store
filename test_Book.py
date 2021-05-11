import unittest
import shop
import numpy as np


class TestBook(unittest.TestCase):

    def setUp(self):
        potatos = shop.StockUnit("potatos", 9, "kg", "Something...")
        eggs = shop.StockUnit("eggs", 10, "pieces", "something...")
        milk = shop.StockUnit("milk", 5, "l", "something...")
        self.test_stock = shop.Stock()
        self.test_stock.add_item(1, potatos, 12, 100)
        self.test_stock.add_item(2, eggs, 25, 100)
        self.test_stock.add_item(3, milk, 10, 100)

        self.test_book = shop.Book("testBook")
        self.test_receipt_sale1 = shop.Receipt([(1, 2), (2, 2), (3, 3)], self.test_stock)
        self.test_receipt_sale2 = shop.Receipt([(1, 4), (2, 3), (3, 2)], self.test_stock)
        self.test_receipt_purc1 = shop.Receipt([(1, 30), (2, 30), (3, 40)], self.test_stock, purchase_sale="p")
        self.test_receipt_purc2 = shop.Receipt([(1, 10), (2, 10), (3, 20)], self.test_stock, purchase_sale="p")

        self.test_book.add_receipt(self.test_receipt_sale1)
        self.test_book.add_receipt(self.test_receipt_sale2)
        self.test_book.add_receipt(self.test_receipt_purc1)
        self.test_book.add_receipt(self.test_receipt_purc2)

        self.test_book.print_todays_receipts()

    def test_add_receipt(self):        
        self.assertEqual(self.test_receipt_sale1, self.test_book.day_receipts[0])
        self.assertEqual(self.test_receipt_purc1, self.test_book.day_receipts[2])

    def test_find_day_costs(self):
        self.test_book.find_day_costs()
        self.assertEqual(self.test_book.day_costs, self.test_receipt_purc1.total + self.test_receipt_purc2.total)

    def test_find_day_sales(self):
        self.test_book.find_day_sales()
        self.assertEqual(self.test_book.day_sales, self.test_receipt_sale1.total + self.test_receipt_sale2.total)

    def test_find_day_sales(self):
        self.test_book.find_day_balance()
        self.assertEqual(self.test_book.day_balance, self.test_receipt_sale1.total + self.test_receipt_sale2.total - self.test_receipt_purc1.total - self.test_receipt_purc2.total)

    def test_store_balance(self):
        self.test_book.store_balance()
        with open("testBook_balance_history.csv", "r") as file:
            for line in file:
                pass
            last_line = line[:-1].split(" ")
        self.assertEqual(int(last_line[4]), self.test_receipt_sale1.total + self.test_receipt_sale2.total - self.test_receipt_purc1.total - self.test_receipt_purc2.total)

    def test_store_todays_receipts(self):
        self.test_book.store_todays_receipts()
        with open("testBook_receipts.csv", "r") as file:
            for line in file:
                pass
            last_line = line[:-1].split(" ")
        self.assertEqual(int(last_line[2]), self.test_receipt_purc2.total)

if __name__ == '__main__':
    unittest.main()