import shop
import pytest

def test_Purchase():
    stock1 = shop.Stock()
    stock2 = shop.Stock()
    mælk = shop.StockUnit("mælk", 2.50, "liter")
    kaffe = shop.StockUnit("kaffe", 15.00, "kg")
    stock1.add_item("123", mælk, 7.50, 100)
    stock2.add_item("255", kaffe, 59.95, 20)

    #shop.Purchase("123", 5, stock1, book, account)