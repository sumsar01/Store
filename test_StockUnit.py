import unittest
import shop

class StockUnit_test(unittest.TestCase):

    def setUp(self):
        self.mælk = shop.StockUnit("mælk", 2.50, "liter")
        self.kaffe = shop.StockUnit("kaffe", 15.00, "kg")

    def test_get_information(self):
        self.mælk.get_information
        self.kaffe.get_information

    def test_set_description(self):
        self.mælk.set_description("Mælken fra en ko.")
        self.kaffe.set_description("Malet kaffe i en pose.")
        self.assertEqual(self.mælk.description, "Mælken fra en ko.")
        self.assertEqual(self.kaffe.description, "Malet kaffe i en pose.")

        self.assertRaises(TypeError, self.mælk.set_description, 123)
        self.assertRaises(TypeError, self.kaffe.set_description, 563.77)
        

    def test_set_cost(self):
        self.mælk.set_cost(5.00)
        self.kaffe.set_cost(20.00)
        self.assertEqual(self.mælk.cost, 5.00)
        self.assertEqual(self.kaffe.cost, 20.00)

        self.assertRaises(TypeError, self.mælk.set_cost, "hej")
        self.assertRaises(TypeError, self.kaffe.set_cost, [])


if __name__ == "__main__":
    unittest.main()