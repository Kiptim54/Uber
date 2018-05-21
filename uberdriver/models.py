from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




class Location(models.Model):
    Longitude=models.IntegerField()
    latitude=models.IntegerField()

    def __int__(self):
        return self.Longitude

# Create your models here.
class Car(models.Model):
    Brand=models.CharField(max_length=50)
    numberplate=models.CharField(max_length=50, unique=True)
    seats=models.IntegerField()
    owner=models.OneToOneField(User,on_delete=models.CASCADE)
   

    def save_car(self):
        return self.save()
    

    def __str__(self):
        return self.numberplate


class Driver_profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50, blank=True)
    # pickup=models.ForeignKey(Location)
    car=models.ForeignKey(Car, blank=True)
    phonenumber=models.IntegerField(null=True)
    email_confirmed = models.BooleanField(default=False)

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Driver_profile.objects.create(user=instance)
#     instance.driver_profile.save()
    
    
    def profile_save(self):
        self.save()

  


    def __str__(self):
        return self.name

class Destination(models.Model):
    serial_number = models.AutoField(primary_key=True)
    destination=models.CharField(max_length=50)
    leaving_time=models.DateTimeField()
    driver=models.ForeignKey(Driver_profile)
    bookers=models.ManyToManyField(User, blank=True, related_name='passgers')

    def save_destination(self):
        self.save()

    @classmethod
    def display_destinations(cls, driver):
        destinations=cls.objects.all().filter(driver__user=driver)
        return destinations

    def __int__(self):
        return self.serial_number



