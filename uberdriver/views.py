from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import Create_Profile, Car_profile, Destination_form
from .models import Driver_profile, Destination, Car
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import SignUpForm
from .tokens import account_activation_token
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token


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


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.driver_profile.phone_number = form.cleaned_data.get('Phonenumber')
#             user.driver_profile.car=2
#             user.save()
#             current_site = get_current_site(request)
#             subject = 'Activate Your MySite Account'
#             message = render_to_string('account_activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             user.email_user(subject, message)
#             return redirect('account_activation_sent')
#     else:
#         form = SignUpForm()
#     return render(request, 'driver/signup.html', {"form":form})

# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.Driver_profile.email_confirmed = True
#         user.save()
#         login(request, user)
#         return redirect('home')
#     else:
#         return render(request, 'account_activation_invalid.html')

# def account_activation_sent(request):
#     return redirect(request, 'account_activation_sent.html')