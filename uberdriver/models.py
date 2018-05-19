from django.db import models
from django.contrib.auth.models import User



class Location(models.Model):
    Longitude=models.IntegerField()
    latitude=models.IntegerField()

    def __int__(self):
        return self.Longitude

class Destination(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Driver_profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    # pickup=models.ForeignKey(Location)
    driver_destination=models.ForeignKey(Destination)
    phonenumber=models.IntegerField()
    
    
    def profile_save(self):
        self.save()

    def __str__(self):
        return self.name

# Create your models here.
class Car(models.Model):
    Brand=models.CharField(max_length=50)
    numberplate=models.CharField(max_length=50)
    seats=models.IntegerField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def save_car(self):
        return self.save()
    

    def __str__(self):
        return self.Brand


