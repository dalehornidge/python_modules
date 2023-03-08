import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.food import Food

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.coffee_shop = CoffeeShop("Starbucks", 300.00, "Espresso", [])
        self.customer = Customer("David", 45.00, 21, 9)
        self.food = Food("Croissant", 3.50, 3)
    
    def test_coffee_shop_has_name(self):
        self.assertEqual("Starbucks", self.coffee_shop.name)

    def test_can_increase_till(self):
        self.coffee_shop.increase_till(2.50)
        self.assertEqual(302.50, self.coffee_shop.till)

    def test_check_age(self):
        self.assertEqual(True, self.coffee_shop.check_age(self.customer))

    def test_energy_level(self):
        self.assertEqual(True, self.coffee_shop.check_energy(self.customer))

    
    def test_sell_food(self):
        self.coffee_shop.sell_food(self.customer, self.food)
        self.assertEqual(41.50, self.customer.wallet)
        self.assertEqual(303.50, self.coffee_shop.till)
        self.assertEqual(6, self.customer.energy_level)
   

    # def test_get_drink_names(self):

    # def test_drinks_customer_can_afford(self):

