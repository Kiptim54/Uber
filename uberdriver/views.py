from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .email import send_welcome_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import Create_Profile, Car_profile, Destination_form
from .models import Driver_profile, Destination, Car

@login_required
def home_page(request):
    title="Home | Driver"
    '''
    function for the landing page of the driver
    '''
    return render( request, 'driver/index.html', {"title":title})
@login_required
def create_profile(request):
    current_user = request.user
    current_user.id=request.user.id
    car=Car.objects.get(owner=current_user.id)
    print("hello")
    if request.method == 'POST':
        form = Create_Profile(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.car=car
            profile.save()
            return redirect('home_driver')
            
    else:
        form =Create_Profile()
    return render(request, 'driver/profile_edit.html', {"form": form})
@login_required
def car_profile(request):
    current_user = request.user
    print(current_user)
    if request.method == 'POST':
        form = Car_profile(request.POST)
        if form.is_valid():
            car= form.save(commit=False)
            car.owner=current_user
            car.save()
            return redirect('createprofile')
        
    else:
        form =Car_profile()
    return render(request, 'driver/car_edit.html', {"form": form})
@login_required   
def create_destination(request):
    '''
    function used by the driver to set their destination
    '''

    title="Ride | Destination"
    current_user=request.user
    current_user.id=request.user.id
    print(current_user.id)
    print("hello from destination")
    driver_user=Driver_profile.objects.get(user=current_user.id)
    print(driver_user)
    
    if request.method=='POST':
        form=Destination_form(request.POST)
        if form.is_valid():
            destination=form.save(commit=False)
            destination.driver=driver_user
            destination.save()
            return redirect('home_driver')
            
    else:
        form=Destination_form()
    return render(request, 'driver/destination.html', {"form":form, "title":title})

@login_required
def display_destinations(request):
    title="Ride | Destinations "
    current_user=request.user
    driver=request.user.id
    schedules=Destination.display_destinations(driver)
    return render(request, 'driver/schedule.html', {"schedules":schedules, "title":title})
@login_required
def driver_profile(request, id):
    '''
    function to display the driver profile and their past rides
    '''
    title="Ride | Profile"
    id=get_object_or_404(Driver_profile, id=id)
    print(id)
    driver=Driver_profile.objects.get(name=id)
    print(driver)
    return render(request, 'driver/profile.html', {"title":title, "driver":driver})


# def sign_up(request):
#     if request.method=='POST':
#         form =UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data.get('username')
#             raw_password=form.cleaned_data.get('password1')
#             email=form.cleaned_data['email']
#             print(email)
#             print("hello")
            
#             user=authenticate(username=username, password=raw_password)
#             send_welcome_email(username,email)
#             print("sent")
#             login(request, user)
            
#             return redirect('home')
#     else:
#         form=UserCreationForm()
#     return render(request, 'driver/signup.html', {"form":form})
