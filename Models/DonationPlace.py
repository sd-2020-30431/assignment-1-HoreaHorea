class DonationPlace:

    def __init__(self, name: str, location: str, contact: str):
        self.name = name
        self.location = location
        self.contact = contact

    def __repr__(self):
        return "NGO named {} which is located at {} and can be contacted by {}"\
            .format(self.name, self.location, self.contact)


