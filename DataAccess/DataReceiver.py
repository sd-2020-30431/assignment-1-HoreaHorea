from DataAccess.DonationPlaceDB import DonationPlaceDB
from DataAccess.FoodItemDB import FoodItemDB
from Models import Today
from Models.DonationPlace import DonationPlace
from Models.FoodItem import FoodItem
from Models.Today import now_date, tomorrow
from WorkLayer.MonthlyReportFactory import MonthlyReportFactory
from WorkLayer.WeeklyReportFactory import WeeklyReportFactory

db = "WasteLess.db"


class DataReceiver:

    def __init__(self, reqtype, data):
        self.fidb = FoodItemDB(db)
        if reqtype == "Food item":
            self.fidb.insFood(FoodItem(*data[0:5]))
        if reqtype == "Donation place":
            dpdb = DonationPlaceDB(db)
            dpdb.insDonationPlace(DonationPlace(*data[0:3]))
        if reqtype == "Eaten item":
            self.fidb.insFood(FoodItem(data[0], '-' + data[1], 1, Today.now_date, Today.now_date))
        if reqtype == "Donated item":
            self.fidb.insFood(FoodItem(data[1], '-' + data[2], 1, Today.now_date, Today.now_date))

        if reqtype == "Weekly report":
            wrf = WeeklyReportFactory(*data[0:2], self.fidb)
            wrf.createReport()
            data[2].delete(0,'end')
            data[2].insert(0,'That week you ate {} calories, but wasted {}. At least you donated {}kg to charity!'
                           .format(*wrf.report))

        if reqtype == "Monthly report":
            mrf = MonthlyReportFactory(*data[0:2], self.fidb)
            mrf.createReport()
            data[2].delete(0,'end')
            data[2].insert(0,'That month you ate {} calories, but wasted {}. At least you donated {}kg to charity!'
                           .format(*mrf.report))

        if reqtype == "Next day":
            tomorrow()
            self.fidb.updateFoodByExpDate(now_date)

    def __call__(self, *args):
        if len(args) != 3:
            return
        self.__init__(*args)
        # if reqtype == "Goal":
        #     godb = FoodItemDB(db)
        #     godb.insFood(FoodItem(data[0:4]))
