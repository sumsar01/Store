import shop
import pytest

def test_Purchase():
    stock1 = shop.Stock()
    stock2 = shop.Stock()
    mælk = shop.StockUnit("mælk", 2.50, "liter")
    kaffe = shop.StockUnit("kaffe", 15.00, "kg")
    stock1.add_item("123", mælk, 7.50, 100)
    stock2.add_item("255", kaffe, 59.95, 20)
    book1 = shop.Book()
    account1 = shop.Account(2000)
    book2 = shop.Book()
    account2 = shop.Account(2000)


    shop.Purchase("123", 50, stock1, book1, account1)
    shop.Purchase("255", 5, stock2, book2, account2)

    assert account1.get() == (2000 - 50*2.50)
    assert account2.get() == (2000 - 5*15.00)

    assert stock1.stock["123"][2] == 150
    assert stock2.stock["255"][2] == 25

    #mangler at tæste at regningen er der
    #mangler at teste for en liste af inputs