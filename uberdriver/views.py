from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm



def home_page(request):
    '''
    function for the landing page of the driver
    '''
    return HttpResponse("Hello Driver welcome to uber")

def sign_up(request):
    if request.method=='POST':
        form =SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            
            user=authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form=SignUpForm()
    return render(request, 'driver/signup.html', {"form":form})
