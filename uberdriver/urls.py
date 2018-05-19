from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_driver'),
    url(r'^profile$', views.create_profile, name='createprofile'),
    url(r'^profile/car', views.car_profile, name='carprofile'),
    url(r'^destination$', views.create_destination, name='driverdestination'),
    url(r'^schedules/', views.display_destinations, name='driver_destinations')

    

]