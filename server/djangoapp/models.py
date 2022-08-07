from django.db import models
from django.utils.timezone import now

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100, default='Make')
    description = models.CharField(max_length=500)

    def __str__(self):
        return "Name: " + self.name

class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    MINIVAN = 'Minivan'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (MINIVAN, 'Minivan')
    ]

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=100, default='Model')
    dealerId = models.IntegerField(default=1)
    type = models.CharField(choices=CAR_TYPES, max_length=10, default=SEDAN)
    year = models.DateField()

    def __str__(self):
        return "Name: " + self.name + ", " + \
            "Dealer Id " + str(self.dealerId) + ", " + \
            "Type: " + self.type + ", " + \
            "Year" + str(self.year)

class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, state, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state abbreviation
        self.st = st
        # Dealer state
        self.state = state
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name
# <HINT> Create a plain Python class `DealerReview` to hold review data

class DealerReview:

    def __init__(self, dealership, name, id, review, purchase, purchase_date="", car_make="", car_model="", car_year="", sentiment=""):
        # Reviewed dealership
        self.dealership = dealership
        # Reviewer Name
        self.name = name
        # Review id
        self.id = id
        # Review
        self.review = review
        # Reviewed purchase
        self.purchase = purchase
        # Reviewed purchase date
        self.purchase_date = purchase_date
        # Reviewed car make
        self.car_make = car_make
        # Reviewed car model
        self.car_model = car_model
        # Reviewed car year
        self.car_year = car_year
        # Sentiment of the review
        self.sentiment = sentiment

    def __str__(self):
        return "review: " + self.review + "by: " + self.name