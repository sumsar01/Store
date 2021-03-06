import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
import shop


class TestReceipt(unittest.TestCase):

    def setUp(self):
        eggs = shop.StockUnit("Eggs", 18, "stk", "Expensive eggs")
        potatoes = shop.StockUnit("Potatoes", 10, "kg", "Danish potatoes")
        self.test_stock = shop.Stock()
        self.test_stock.add_item(1, eggs, 25, 50)
        self.test_stock.add_item(2, potatoes, 15, 30)
        id_q_list = [(1, 2), (2, 2)]
        self.test_receipt = shop.Receipt(id_q_list, self.test_stock, purchase_sale="s")

    def test_calc_item_pricecost(self):
        total_price_of_eggs = self.test_receipt.item_entries[0][2]
        total_price_of_potatoes = self.test_receipt.item_entries[1][2]

        self.assertEqual(total_price_of_eggs, 50)
        self.assertEqual(total_price_of_potatoes, 30)

    def test_make_full_item_entries(self):
        receipt_list = self.test_receipt.item_entries

        self.assertEqual(receipt_list, [(1, 2, 50), (2, 2, 30)])

    def test_calc_total(self):
        expected_total = 80
        actual_total = self.test_receipt.total

        self.assertEqual(actual_total, expected_total)


if __name__ == '__main__':
    unittest.main()