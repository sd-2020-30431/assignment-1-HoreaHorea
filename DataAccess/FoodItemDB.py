import sqlite3


class FoodItemDB:

    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)
        self.c = self.conn.cursor()
        self.c.execute(" create table if not exists Foods ("
                       "        name text,"
                       "        quantity real,"
                       "        calories real,"
                       "        buy_date text,"
                       "        exp_date text"
                       "        )")

    def drop(self):
        self.c.execute("drop table Foods")

    def getFoodsByName(self):
        with self.conn:
            self.c.execute("select * from Foods order by name")
            return self.c.fetchall()

    def getFoodsByExpDate(self):
        with self.conn:
            self.c.execute("select * from Foods order by exp_date")
            return self.c.fetchall()

    def insFood(self, item):
        with self.conn:
            self.c.execute("insert into Foods\n"
                           "values (:name,:quantity,:calories,:buy_date,:exp_date)",
                           {'name': item.name,
                            'quantity': item.quantity,
                            'calories': item.calories100g,
                            'buy_date': item.buy_date,
                            'exp_date': item.exp_date})
            return self.c.fetchone()

    def delFoodByDate(self, exp_date):
        with self.conn:
            self.c.execute("delete from Foods where\n"
                           "(exp_date = :exp_date)",
                           {'exp_date': exp_date})
            return self.c.fetchall()

    # def updateFoodByDate(self, new_exp_date):
    #     with self.conn:
    #         self.c.execute("update Foods set buy_date\n"
    #                        "(exp_date = :exp_date)",
    #                        {'exp_date': exp_date})

    def updateFoodByDate(self, new_exp_date):
        with self.conn:
            self.c.execute("update Foods set buy_date\n"
                           "(exp_date = :exp_date)",
                           {'exp_date': exp_date})

    # print(getFoodsByName())
    # insFood(FoodItem('a',1,1,"2020-01-04","2020-01-04"))
    # insFood(FoodItem('c',1,1,"2020-01-02","2020-01-02"))
    # insFood(FoodItem('b',1,1,"2020-01-03","2020-01-03"))
    #
    # print(getFoodsByName())
    # print(getFoodsByExpDate())
    #
    # delFoodByDate("2020-01-03")
    #
    #
    # print(getFoodsByName())
    # print(getFoodsByExpDate())
    # self.c.execute("INSERT INTO Foods VALUES (:first,:last,:pay)",
    #           {'first': emp1.first, 'last': emp1.last, 'pay': emp1.pay})

    # self.c.execute("INSERT INTO employees VALUES ('Ana','AreMere','500')")

    # def getFoodsByName(item):
    #     with self.conn:
    #         self.c.execute("select * from Foods where name = :name ", {'name': name})
    #         return self.c.fetchall()
