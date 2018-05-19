from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome_user(request):
    '''
    function for the landing page of the driver
    '''
    return render(request, 'joint/joint.html')
