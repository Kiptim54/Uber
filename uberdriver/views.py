from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .email import send_welcome_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import Create_Profile, Car_profile

@login_required
def home_page(request):
    '''
    function for the landing page of the driver
    '''
    return HttpResponse("Hello Driver welcome to uber")

def create_profile(request):
    current_user = request.user.id
    print("hello")
    if request.method == 'POST':
        form = Create_Profile(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            print("hello")
            print(profile)
    else:
        form =Create_Profile()
    return render(request, 'driver/profile_edit.html', {"form": form})

def car_profile(request):
    current_user = request.user.id
    if request.method == 'POST':
        form = Car_profile(request.POST)
        
        car= form.save()
        car.profile=current_user.id
        car.save()
        return redirect('/driver/profile')
    else:
        form =Car_profile()
    return render(request, 'driver/car_edit.html', {"form": form})
    


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
