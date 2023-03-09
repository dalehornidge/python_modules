import unittest
from src.customer import Customer
from src.drink import Drink
from src.coffee_shop import CoffeeShop
from tests.coffee_shop_test import TestCoffeeShop

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("James", 100.00, 21, 0)
        self.drink = Drink("Latte", 2.50, 2, True)
        self.coffee_shop = CoffeeShop("Starbucks", 1000, "drink", [])

    def test_customer_has_name(self):
        self.assertEqual("James", self.customer.name)

    def test_decrease_wallet(self):
        self.customer.decrease_wallet(2.50)
        self.assertEqual(97.50, self.customer.wallet)

    def test_energy_level_increase(self):
        self.customer.increase_energy_level(self.drink)
        self.assertEqual(2, self.customer.energy_level)

    def test_buy_drink(self):
        self.customer.buy_drink(self.drink, self.coffee_shop)
        self.assertEqual(97.50, self.customer.wallet)
        self.assertEqual(21, self.customer.age)
        self.assertEqual(2, self.customer.energy_level)
        self.assertEqual(1002.50, self.coffee_shop.till)
      