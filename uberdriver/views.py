from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    '''
    function for the landing page of the driver
    '''
    return HttpResponse("Hello Driver welcome to uber")
