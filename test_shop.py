import unittest
import shop

    """
    Stock item.

    StockUnit(name, cost, unit, description = "")
    name - name of item
    cost - cost of buying item home to the shop
    unit - the unit of the item
    description - a short description of the item


    Methods:

    get_information(verbose = False)
        prints the information on the item.
        if verbose is True more information is given.

    set_description(new_description)
        set a new description of the item.

    set_cost(new_cost)
        set a new cost of the item.

    """


class StockUnit_test(unittest.TestCase):

    def setUp(self):
        mælk = StockUnit("mælk", "2.50", "liter")
        kaffe = StockUnit("kaffe", "15.00", "kg")

    def test_get_information(self):
        mælk.get_information
        kaffe.get_information

    def test_set_description(self):
        mælk.set_description("Mælken fra en ko.")
        kaffe.set_description("Malet kaffe i en pose.")
        assert(mælk.description == "Mælken fra en ko.")
        assert(kaffe.description == "Malet kaffe i en pose.")

    def test_set_cost(self):
        pass




if __name__ == "__main__":
    pass


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