from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
    '''
    function for the landing page of the customer
    '''
    title="Ride | Customer "
    return render(request, 'customer/index.html', {"title":title})
