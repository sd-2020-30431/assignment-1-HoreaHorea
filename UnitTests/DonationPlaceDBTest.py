import unittest

from DataAccess.DonationPlaceDB import DonationPlacesDB
from Models.DonationPlace import DonationPlace
from WorkLayer.Verifier import Verifier


class FoodItemDBTest(unittest.TestCase):

    def setUp(self):
        v = Verifier()
        self.db = DonationPlacesDB(":memory:")
        a = DonationPlace('Red Cross', 'Everywhere', 'Local RC/312093812')
        b = DonationPlace('Smurd', 'Tg. Mures', 'No Contact')
        c = DonationPlace('Amnesty International', 'Syria', '888-8888')

        if v.donationPlaceVerifier(a):
            self.db.insDonationPlace(a)
        if v.donationPlaceVerifier(b):
            self.db.insDonationPlace(b)
        if v.donationPlaceVerifier(c):
            self.db.insDonationPlace(c)

    def tearDown(self):
        self.db.drop()

    def test_del(self):
        self.db.delDonationPlaces('Red Cross')
        self.db.delDonationPlaces('Smurd')
        self.db.delDonationPlaces('Amnesty International')
        res = self.db.getDonationPlaces()
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
