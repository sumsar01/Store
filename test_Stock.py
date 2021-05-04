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
    
    with pytest.raises(ValueError):
        stock1.add_item("123", mælk, 7.50, 100)
    with pytest.raises(ValueError):
        stock2.add_item("255", kaffe, 59.95, 20)
    
    del stock1
    del stock2

def test_use_item():
    stock1 = shop.Stock()
    stock2 = shop.Stock()
    mælk = shop.StockUnit("mælk", 2.50, "liter")
    kaffe = shop.StockUnit("kaffe", 15.00, "kg")
    stock1.add_item("123", mælk, 7.50, 100)
    stock2.add_item("255", kaffe, 59.95, 20)

    stock1.use_item("123", 10)
    stock2.use_item("255", 5)

    assert stock1.stock["123"][2] == 90
    assert stock2.stock["255"][2] == 15

    with pytest.raises(ValueError):
        stock1.use_item("133", 10)
    with pytest.raises(ValueError):
        stock2.use_item("275", 5) 

    with pytest.raises(TypeError):
        stock1.use_item("123", "hej")
    with pytest.raises(TypeError):
        stock2.use_item("255", []) 

    del stock1
    del stock2

def test_update_stock():
    stock1 = shop.Stock()
    stock2 = shop.Stock()
    mælk = shop.StockUnit("mælk", 2.50, "liter")
    kaffe = shop.StockUnit("kaffe", 15.00, "kg")
    stock1.add_item("123", mælk, 7.50, 100)
    stock2.add_item("255", kaffe, 59.95, 20)

    stock1.update_stock("123", 10)
    stock2.update_stock("255", 5)

    assert stock1.stock["123"][2] == 110
    assert stock2.stock["255"][2] == 25

    with pytest.raises(ValueError):
        stock1.update_stock("133", 10)
    with pytest.raises(ValueError):
        stock2.update_stock("275", 5) 

    with pytest.raises(TypeError):
        stock1.update_stock("123", "hej")
    with pytest.raises(TypeError):
        stock2.update_stock("255", [])   

    del stock1
    del stock2  


def test_delete_item():
    stock1 = shop.Stock()
    stock2 = shop.Stock()
    mælk = shop.StockUnit("mælk", 2.50, "liter")
    kaffe = shop.StockUnit("kaffe", 15.00, "kg")
    stock1.add_item("123", mælk, 7.50, 100)
    stock2.add_item("255", kaffe, 59.95, 20)

    stock1.delete_item("123")
    stock2.delete_item("255")

    assert stock1.stock == {}
    assert stock2.stock == {}

    with pytest.raises(ValueError):
        stock1.delete_item("123")
    with pytest.raises(ValueError):
        stock2.delete_item("255")

    del stock1
    del stock2


def test_stock_information():
    stock1 = shop.Stock()
    stock2 = shop.Stock()
    mælk = shop.StockUnit("mælk", 2.50, "liter")
    kaffe = shop.StockUnit("kaffe", 15.00, "kg")
    stock1.add_item("123", mælk, 7.50, 100)
    stock2.add_item("255", kaffe, 59.95, 20)

    stock1.stock_information()
    stock2.stock_information()

    del stock1
    del stock2

def test_get_price():
    stock1 = shop.Stock()
    stock2 = shop.Stock()
    mælk = shop.StockUnit("mælk", 2.50, "liter")
    kaffe = shop.StockUnit("kaffe", 15.00, "kg")
    stock1.add_item("123", mælk, 7.50, 100)
    stock2.add_item("255", kaffe, 59.95, 20)

    assert stock1.get_price("123") == 7.50
    assert stock2.get_price("255") == 59.95

    with pytest.raises(ValueError):
        stock1.get_price("133")
    with pytest.raises(ValueError):
        stock2.get_price("275")

    del stock1
    del stock2

def test_get_cost():
    stock1 = shop.Stock()
    stock2 = shop.Stock()
    mælk = shop.StockUnit("mælk", 2.50, "liter")
    kaffe = shop.StockUnit("kaffe", 15.00, "kg")
    stock1.add_item("123", mælk, 7.50, 100)
    stock2.add_item("255", kaffe, 59.95, 20)

    assert stock1.get_cost("123") == 2.50
    assert stock2.get_cost("255") == 15.00

    with pytest.raises(ValueError):
        stock1.get_cost("133")
    with pytest.raises(ValueError):
        stock2.get_cost("275")

    del stock1
    del stock2

def test_get_item():
    stock1 = shop.Stock()
    stock2 = shop.Stock()
    mælk = shop.StockUnit("mælk", 2.50, "liter")
    kaffe = shop.StockUnit("kaffe", 15.00, "kg")
    stock1.add_item("123", mælk, 7.50, 100)
    stock2.add_item("255", kaffe, 59.95, 20)

    assert stock1.get_item("123") == mælk
    assert stock2.get_item("255") == kaffe

    with pytest.raises(ValueError):
        stock1.get_cost("133")
    with pytest.raises(ValueError):
        stock2.get_cost("275")

    del stock1
    del stock2

