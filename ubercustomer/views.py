from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from uberdriver.models import Driver_profile, Destination, Car,Location
from .models import Passenger_profile

# Create your views here.
def home_page(request):
    '''
    function for the landing page of the customer
    '''
    title="Ride | Customer "
    return render(request, 'customer/index.html', {"title":title})

def display_rides(request):
    '''
    function that displays all available rides to the customer
    '''
    title="Rides | Available rides"
    rides=Destination.objects.all()
    print(rides)
    return render(request, 'customer/all_rides.html', {"title":title, "rides":rides})
