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

# <HINT> Create a plain Python class `CarDealer` to hold dealer data

# <HINT> Create a plain Python class `DealerReview` to hold review data
