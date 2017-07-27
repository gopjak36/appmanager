from django.shortcuts import render

from .models import Appointment

def appointments_list(request):
    ''' Appointments List method '''

    return render(request, 'manager/appointments_list.html', {'appointments': Appointment.objects.all()})

def appointments_add(request):
    ''' Appointments Add method '''

    return render(request,'manager/appointments_add.html',{})
