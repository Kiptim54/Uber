from django.db import models

# Create your models here.
class Car(models.Model):
    Brand=models.CharField()
    numberplate=models.CharField()
    seats=models.IntegerField()

class Location(models.Model):
    Longitude=models.IntegerField()
    latitude=models.IntegerField()

class Destination(models.Model):
    name=models.CharField()

class Driver(models.Model):
    name=models.CharField(max_length=50)
    car=models.ForeignKey(Car)
    pickup=models.ForeignKey(Location)
    driver_destination=models.ForeignKey(Destination)

class Passenger(models.Model):
    name=models.CharField(max_length=50)
    location=models.ForeignKey(Location)
    pickupoint=models.ForeignKey(Location)
    passenger_destination=models.ForeignKey(Destination)