from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
    '''
    function for the landing page of the driver
    '''
    return HttpResponse("Hello Customer welcome to uber")
