from django.contrib import admin

from .models  import Location, Driver_profile, Destination , Car


admin.site.register(Driver_profile)
admin.site.register(Location)
admin.site.register(Destination)
admin.site.register(Car)