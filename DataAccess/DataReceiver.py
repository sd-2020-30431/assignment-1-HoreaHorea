from DataAccess.FoodItemDB import FoodItemDB
from DataAccess.DonationPlaceDB import DonationPlaceDB
from Models import Today
from Models.DonationPlace import DonationPlace
from Models.FoodItem import FoodItem

db = "WasteLess.db"


class DataReceiver():
    def __init__(self, datatype, data):
        if datatype == "Food item":
            fidb = FoodItemDB(db)
            fidb.insFood(FoodItem(*data[0:5]))
        if datatype == "Donation place":
            dpdb = DonationPlaceDB(db)
            dpdb.insDonationPlace(DonationPlace(*data[0:3]))
        if datatype == "Eaten item":
            fidb = FoodItemDB(db)
            print(data)
            fidb.insFood(FoodItem(data[0], '-'+data[1], 0, Today.now_date, Today.now_date))
        if datatype == "Donated item":
            fidb = FoodItemDB(db)
            print(data)
            fidb.insFood(FoodItem(data[1], '-'+data[2], 0, Today.now_date, Today.now_date))
        # if datatype == "Goal":
        #     godb = FoodItemDB(db)
        #     godb.insFood(FoodItem(data[0:4]))
