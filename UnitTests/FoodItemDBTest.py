import unittest
from Models.FoodItem import FoodItem
from DataAccess.FoodItemDB import FoodItemDB


class TestFoodItem(unittest.TestCase):

    def setUp(self):
        self.db = FoodItemDB(":memory:")
        self.db.insFood(FoodItem('goodFood', 500, 333, '2020-01-01', '2020-01-03'))
        self.db.insFood(FoodItem('badFood', 500, 333, '2020-01-03', '2020-01-01'))
        self.db.insFood(FoodItem('newFood', 500, 333, '2020-01-02', '2020-01-02'))

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
