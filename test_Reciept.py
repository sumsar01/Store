import unittest
import shop

class TestReciept(unittest.TestCase):

    def setUp(self):
        potatoes = shop.StockUnit("Potatoes", 10, "kg", "Danish potatoes")
        eggs = shop.StockUnit("Eggs", 18, "stk", "Expensive eggs")

    def test_calc_item_pricecost(self):
        pass

    def test_make_full_item_entries(self):
        pass

    def test_calc_total(self):
        pass




if __name__ == '__main__':
    unittest.main()