from django.contrib import admin

from .models import Appointment, MultiTime, SubmitData

# Register Appointment Model:
admin.site.register(Appointment)
# Register MultiTime Model:
admin.site.register(MultiTime)
# Register SubmitData Model:
admin.site.register(SubmitData)
