import unittest
from src.food import Food

class TestFood(unittest.TestCase):
        def setUp(self):
            self.food = Food("Croissant", 3.50, 3)

        def test_food_has_name(self):
               self.assertEqual("Croissant", self.food.name)

        def test_food_has_price(self):
               self.assertEqual(3.50, self.food.price)

        def test_food_has_rejuvinate(self):
               self.assertEqual(3, self.food.rejuvinate)





