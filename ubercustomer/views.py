from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from uberdriver.models import Driver_profile, Destination, Car,Location
from .models import Passenger_profile

# Create your views here.
@login_required
def home_page(request):
    '''
    function for the landing page of the customer
    '''
    title="Ride | Customer "
    return render(request, 'customer/index.html', {"title":title})
@login_required
def display_rides(request):
    '''
    function that displays all available rides to the customer
    '''
    title="Rides | Available rides"
    
    rides=Destination.objects.all()
    print(rides)
    return render(request, 'customer/all_rides.html', {"title":title, "rides":rides})

def book_ride(request, id):
    '''
    function for a passenger to book a ride
    '''
    current_user=request.user 
    id=get_object_or_404(Destination, serial_number=id)
    print(id)
    destination=Destination.objects.get(serial_number=id)
    print(destination)
    destination.bookers.add(current_user)
    destination.save()
    return redirect ('available_rides')
