from datetime import timedelta, date


class FoodItem:
    """First class"""

    def __init__(self, name: str, quantity: float, calories: float, buy_date: str, exp_date: str) -> object:
        self.name = name
        self.quantity = quantity
        self.calories100g = calories
        self.buy_date = buy_date
        self.exp_date = exp_date

    @property
    def isExpired(self):
        if (date.fromisoformat(self.exp_date) - date.fromisoformat(self.buy_date)).days < 0:
            return True
        return False

    @property
    def totalCalories(self):
        return self.calories100g * self.quantity / 100

    @property
    def optimalCaloriesEachDay(self):
        if not self.isExpired:
            return self.totalCalories / (
                    (date.fromisoformat(self.exp_date) - date.fromisoformat(self.buy_date)).days + 1)
        else:
            return 0

    def __repr__(self):
        return "Food {} contains a total of {} calories at a {} caloric density / 100g, and was bought on{} while it " \
               "expires on {})".format(
            self.name, self.quantity, self.calories100g, self.buy_date, self.exp_date)


ana = FoodItem('', 12, 133, '2000-01-02', '2000-01-01')
print(ana.isExpired)
