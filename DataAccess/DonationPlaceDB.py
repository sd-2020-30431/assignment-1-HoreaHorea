import sqlite3


class DonationPlaceDB:

    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)
        self.c = self.conn.cursor()

        self.c.execute(" create table if not exists DonationPlaces ("
                       "        name text,"
                       "        location text,"
                       "        contact text"
                       "        )")

    def drop(self):
        self.c.execute("drop table DonationPlaces")

    def getDonationPlaces(self):
        with self.conn:
            self.c.execute("select * from DonationPlaces order by name")
            return self.c.fetchall()

    def insDonationPlace(self, place):
        with self.conn:
            self.c.execute("insert into DonationPlaces\n"
                           "values (:name,:location,:contact)",
                           {'name': place.name,
                            'location': place.location,
                            'contact': place.contact})
            return self.c.fetchone()

    def delDonationPlaces(self, name):
        with self.conn:
            self.c.execute("delete from DonationPlaces where\n"
                           "(name = :name)",
                           {'name': name})
            return self.c.fetchall()

