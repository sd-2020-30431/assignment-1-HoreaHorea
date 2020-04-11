import unittest
from Models.FoodItem import FoodItem


class FoodItemTest(unittest.TestCase):

    def setUp(self):
        self.goodFood = FoodItem ('goodFood', 500, 333, '2020-04-11', '2020-04-18')
        self.nowFood = FoodItem("nowFood", 500, 333, "2020-04-11", "2020-04-12")
        self.badFood = FoodItem("badFood", 500, 333, "2020-04-11", "2020-04-10")

    def tearDown(self):
        pass

    def test_expire(self):
        self.assertFalse(self.goodFood.isExpired)
        self.assertFalse(self.nowFood.isExpired)
        self.assertTrue(self.badFood.isExpired)

    def test_calorieDistribution(self):
        self.assertEqual(self.badFood.optimalCaloriesEachDay, 0)
        self.assertGreater(self.nowFood.optimalCaloriesEachDay, 0)

    def test_print(self):
        # irrelevant though
        self.assertIsNone(print(self.goodFood))



if __name__ == '__main__':
    unittest.main()
