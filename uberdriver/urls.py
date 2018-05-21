from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_driver'),
    url(r'^profile/edit/$', views.create_profile, name='createprofile'),
    url(r'^profile/car', views.car_profile, name='carprofile'),
    url(r'^destination$', views.create_destination, name='driverdestination'),
    url(r'^schedules/', views.display_destinations, name='driver_destinations'),
    url(r'^profile/(?P<id>\d+)', views.driver_profile, name='driver_profile'),
    # url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
    # url(r'^signup/$', views.signup, name='signup')
    

    

]