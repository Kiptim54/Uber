from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Driver_profile, Car, Destination


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class Create_Profile(forms.ModelForm):
    class Meta:
        model=Driver_profile
        fields=['name', 'phonenumber']

class Car_profile(forms.ModelForm):
    class Meta:
        model=Car
        fields=['Brand', 'numberplate', 'seats']

class Destination_form(forms.ModelForm):
    class Meta:
        model=Destination
        fields=['destination', 'leaving_time']