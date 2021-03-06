from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^rides/$', views.display_rides, name='available_rides'),
    url(r'^rides/book/(?P<id>\d+)$', views.book_ride, name='book_ride'),
]