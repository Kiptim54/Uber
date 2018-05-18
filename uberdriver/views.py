from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .email import send_welcome_email
from django.contrib.auth.models import User


def home_page(request):
    '''
    function for the landing page of the driver
    '''
    return HttpResponse("Hello Driver welcome to uber")

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
