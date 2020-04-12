import unittest
from Models.FoodItem import FoodItem
from DataAccess.FoodItemDB import FoodItemDB
from WorkLayer.Verifier import Verifier


class FoodItemDBTest(unittest.TestCase):

    def setUp(self):
        v = Verifier()
        self.db = FoodItemDB(":memory:")
        a = FoodItem('goodFood', 500, 333, '2020-01-01', '2020-01-03')
        b = FoodItem('badFood', 500, 333, '2020-01-03', '2020-01-01')
        c = FoodItem('newFood', 500, 333, '2020-01-02', '2020-01-02')

        if v.foodItemVerifier(a):
            self.db.insFood(a)
        if v.foodItemVerifier(b):
            self.db.insFood(b)
        if v.foodItemVerifier(c):
            self.db.insFood(c)

    def tearDown(self):
        self.db.drop()

    def test_del(self):
        self.db.delFoodByDate('2020-01-01')
        self.db.delFoodByDate('2020-01-02')
        self.db.delFoodByDate('2020-01-03')
        res = self.db.getFoodsByExpDate()
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
