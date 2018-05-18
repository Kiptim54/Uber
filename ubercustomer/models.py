from django.db import models
from uberdriver.models import Location, User, Destination

class Passenger_profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    name=models.CharField(max_length=50)
    location=models.ForeignKey(Location ,related_name='passenger_location')
    pickupoint=models.ForeignKey(Location)
    passenger_destination=models.ForeignKey(Destination)

    def __str__(self):
        return self.name
