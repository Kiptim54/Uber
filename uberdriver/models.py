from django.db import models
from django.contrib.auth.models import User




class Location(models.Model):
    Longitude=models.IntegerField()
    latitude=models.IntegerField()

    def __int__(self):
        return self.Longitude



class Driver_profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    # pickup=models.ForeignKey(Location)
    
    phonenumber=models.IntegerField()
    
    
    def profile_save(self):
        self.save()

    def __str__(self):
        return self.name

class Destination(models.Model):
    destination=models.CharField(max_length=50)
    leaving_time=models.DateTimeField()
    driver=models.ForeignKey(Driver_profile)

    def save_destination(self):
        self.save()

    @classmethod
    def display_destinations(cls, driver):
        destinations=cls.objects.all().filter(driver__user=driver)
        return destinations

    def __str__(self):
        return self.destination

# Create your models here.
class Car(models.Model):
    Brand=models.CharField(max_length=50)
    numberplate=models.CharField(max_length=50)
    seats=models.IntegerField()
    owner=models.OneToOneField(User,on_delete=models.CASCADE)

    def save_car(self):
        return self.save()
    

    def __str__(self):
        return self.Brand


