import shop
import pytest
import os

def test_Sale():
    stock1 = shop.Stock()
    stock2 = shop.Stock()
    mælk = shop.StockUnit("mælk", 2.50, "liter")
    kaffe = shop.StockUnit("kaffe", 15.00, "kg")
    stock1.add_item("123", mælk, 7.50, 100)
    stock1.add_item("255", kaffe, 59.95, 20)
    stock2.add_item("255", kaffe, 59.95, 20)
    stock2.add_item("123", mælk, 7.50, 100)
    book1 = shop.Book("testBook1")
    account1 = shop.Account(2000)
    book2 = shop.Book("testBook2")
    account2 = shop.Account(2000)


    shop.Sale("123", 50, stock1, book1, account1)
    shop.Sale("255", 5, stock2, book2, account2)

    assert account1.get() == (2000 + 50*7.50)
    assert account2.get() == (2000 + 5*59.95)

    assert stock1.stock["123"][2] == 50
    assert stock2.stock["255"][2] == 15

    shop.Sale(["123", "255"] , [5, 2], stock1, book1, account1)

    assert account1.get() == (2000 + 50*7.50 + 5*7.50 + 2*59.95)
    assert stock1.stock["123"][2] == 45
    assert stock1.stock["255"][2] == 18

    shop.Sale(["255", "255"] , [5, 5], stock1, book1, account1)

    assert account1.get() == (2000 + 50*7.50 + 5*7.50 + 2*59.95 + 10*59.95)
    assert stock1.stock["255"][2] == 18-10

    shop.Sale(["255", "123"] , [10, 30], stock2, book2, account2)
    assert account2.get() == (2000 + 5*59.95 + 10*59.95 + 30*7.50)
    assert stock2.stock["123"][2] == 70
    assert stock2.stock["255"][2] == 5

    os.remove("testBook1_balance_history.csv")
    os.remove("testBook1_receipts.csv")
    os.remove("testBook2_balance_history.csv")
    os.remove("testBook2_receipts.csv")