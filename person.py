import faker

fake = faker.Faker()


class Person:
    def __init__(self):
        self.name = fake.name()
        self.date = fake.date()
        self.address = fake.address()
        self.email = fake.email()
        self.company = fake.company()
        self.random_int = fake.random_int()
        self.street_address = fake.street_address()
        self.country = fake.country()

    def jsonformat(self):
        return {
            "name": self.name,
            "date": self.date,
            "address": self.address,
            "email": self.email,
            "company": self.company,
            "random_int": self.random_int,
            "street_address": self.street_address,
            "country": self.country
        }
