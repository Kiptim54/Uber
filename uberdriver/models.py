from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    Brand=models.CharField()
    numberplate=models.CharField()
    seats=models.IntegerField()

    def __str__(self):
        return self.Brand

class Location(models.Model):
    Longitude=models.IntegerField()
    latitude=models.IntegerField()

    def __int__(self):
        return self.Longitude

class Destination(models.Model):
    name=models.CharField()

    def __str__(self):
        return self.name

class Driver_profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    car=models.ForeignKey(Car)
    pickup=models.ForeignKey(Location)
    driver_destination=models.ForeignKey(Destination)

    def __str__(self):
        return self.name


class Passenger_profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    location=models.ForeignKey(Location)
    pickupoint=models.ForeignKey(Location)
    passenger_destination=models.ForeignKey(Destination)

    def __str__(self):
        return self.name