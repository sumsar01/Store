import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import shop
import pytest



def test_Acocunt():
    account1 = shop.Account(1000)
    account2 = shop.Account(2000)

    assert account1.account_holding == 1000
    assert account2.account_holding == 2000

    with pytest.raises(TypeError):
        account1 = shop.Account("hej")
    with pytest.raises(TypeError):
        account2 = shop.Account([])

def test_add_transaction():
    account1 = shop.Account(1000)
    account2 = shop.Account(2000)

    account1.add_transaction(200)
    account2.add_transaction(-500)

    assert account1.account_holding == 1200
    assert account2.account_holding == 1500

    with pytest.raises(TypeError):
        account1.add_transaction("hej")
    with pytest.raises(TypeError):
        account2.add_transaction([])

def test_get():
    account1 = shop.Account(1000)
    account2 = shop.Account(2000)

    assert account1.get() == 1000
    assert account2.get() == 2000