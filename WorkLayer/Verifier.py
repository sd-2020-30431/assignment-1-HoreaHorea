from datetime import timedelta, date
from numbers import Number
from sre_compile import isstring

from Models.DonationPlace import DonationPlace
from Models.FoodItem import FoodItem
import re


class Verifier:

    @staticmethod
    def stringVerifier(elem):
        if not elem or not isstring(elem) or re.search("^[^a-zA-Z0-9 ]*$", elem):
            return False  # Will become error message
        else:
            return True

    @staticmethod
    def numberVerifier(elem):
        if (isinstance(elem, int) or isinstance(elem, float)) and abs(elem) < 1e6:
            return True  # Will become error message
        else:
            return False
    @staticmethod
    def dateVerifier(elem):
        if elem is not None and isstring(elem):
            try:
                date.fromisoformat(elem)
            except Exception:
                return False
            else:
                return True
        else:
            return False

    def FoodItemVerifier(self, item: FoodItem):
        if self.stringVerifier(item.name) \
                and self.numberVerifier(item.calories100g) \
                and self.numberVerifier(item.quantity) \
                and self.dateVerifier(item.buy_date) \
                and self.dateVerifier(item.exp_date):
            return True

    def DonationPlaceVerifier(self, place: DonationPlace):
        if self.stringVerifier(place.name) \
                and self.stringVerifier(place.location) \
                and self.stringVerifier(place.contact):
            return True


# print(type(elem))
# print(isinstance(elem, int))
# print(isinstance(elem, float))