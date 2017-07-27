from django.contrib import admin

from .models import Appointment, MultiTime

# Register Appointment Model:
admin.site.register(Appointment)
# Register MultiTime Model:
admin.site.register(MultiTime)
