import unittest
import shop
import pytest

@pytest.fixture()
def empty_stock():
    return shop.Stock()

def test_stock(empty_stock):
    assert type(empty_stock.stock) is dict

def test_add_item():
    stock1 = shop.Stock()
    stock2 = shop.Stock()
    mælk = shop.StockUnit("mælk", 2.50, "liter")
    kaffe = shop.StockUnit("kaffe", 15.00, "kg")

    stock1.add_item("123", mælk, 7.50, 100)
    stock2.add_item("255", kaffe, 59.95, 20)

    assert stock1.stock == {"123" : [mælk, 7.50, 100]}
    assert stock2.stock == {"255" : [kaffe, 59.95, 20]}

# """ class Stock_test(unittest.TestCase):

#     def setUp(self):
#         self.stock1 = shop.Stock()
#         self.stock2 = shop.Stock()

#     def test_add_item(self):
#         pass

#     def test_use_item(self):
#         pass

#     def test_update_stock(self):
#         pass

#     def test_delete_item(self):
#         pass

#     def test_stock_information(self):
#         pass

#     def test_get_price(self):
#         pass

#     def test_get_cost(self):
#         pass

#     def test_get_item(self):
#         pass """

#if __name__ == "__main__":
#    unittest.main()