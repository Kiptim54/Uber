from django.contrib import admin

from .models  import Location, Driver_profile, Destination 


admin.site.register(Driver_profile)
admin.site.register(Location)
admin.site.register(Destination)