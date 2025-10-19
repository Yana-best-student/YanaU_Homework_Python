class Address:
    def __init__(self, postal_code, city, street, house, apartment):
        self.postal_code = postal_code
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):
        return f"{self.postal_code}, {self.city},"
        return f"{self.street}, {self.house}, {self.apartment}"
