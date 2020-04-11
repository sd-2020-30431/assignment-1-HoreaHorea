from datetime import timedelta, date

<<<<<<< HEAD
from Models import Today
=======
from Models import now_date
>>>>>>> 2b0993318ca20d601c6e0b48c04e84f1ef936884


class FoodItem:
    """First class"""

    def __init__(self, name: str, quantity: float, calories: float, buy_date: str, exp_date: str):
        self.name = name
        self.quantity = quantity
        self.calories100g = calories
        self.buy_date = buy_date
        self.exp_date = exp_date

    @property
    def isExpired(self):
<<<<<<< HEAD
        if (date.fromisoformat(self.exp_date) - Today.now_date.date()).days < 0:
=======
        if (date.fromisoformat(self.exp_date) - now_date).days < 0:
>>>>>>> 2b0993318ca20d601c6e0b48c04e84f1ef936884
            return True
        return False

    @property
    def totalCalories(self):
        return self.calories100g * self.quantity / 100

    @property
    def optimalCaloriesEachDay(self):
        if not self.isExpired:
            return self.totalCalories / (
<<<<<<< HEAD
                    (date.fromisoformat(self.exp_date) - Today.now_date.date()).days + 1)
=======
                    (date.fromisoformat(self.exp_date) - now_date).days + 1)
>>>>>>> 2b0993318ca20d601c6e0b48c04e84f1ef936884
        else:
            return 0

    def __repr__(self):
        return "Food {} contains a total of {} calories at a {} caloric density / 100g, and was bought on{} while it " \
               "expires on {})".format(
            self.name, self.quantity, self.calories100g, self.buy_date, self.exp_date)


