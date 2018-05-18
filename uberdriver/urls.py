from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^signup/' , views.sign_up, name='driversignup'),
    

]