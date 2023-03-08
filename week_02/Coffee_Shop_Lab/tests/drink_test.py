import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Latte", 2.50, 1, True)

    def test_drink_has_name(self):
        self.assertEqual("Latte", self.drink.name)

    def test_drink_price(self):
        self.assertEqual(2.50, self.drink.price)

    def test_drink_available(self):
        self.assertEqual(True, self.drink.availability)