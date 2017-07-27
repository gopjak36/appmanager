from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from datetime import datetime

from .models import Appointment, MultiTime

def appointments_list(request):
    ''' Appointments List method '''

    return render(request, 'manager/appointments_list.html', {'appointments': Appointment.objects.all()})

def appointments_add(request):
    ''' Appointments Add method '''
    # POST == True
    if request.method == 'POST':
        # add button == PUSH:
        if request.POST.get('add_button') is not None:
            data = {} # data collection for Appointment
            multitime = {} # data collection for MultiTime
            errors = {} # erros collection
            postdata = {} # post data coollection

            # Validation data:

            # Title validation:
            title = request.POST.get('title')
            postdata['title'] = title
            if not title:
                errors['title'] = u"Please, enter the Title"
            else:
                data['title'] = title

            # Date validation:
            date = request.POST.get('date')
            postdata['date'] = date
            if not date:
                errors['date'] = u"Please, enter the date."
            else:
                try:
                    datetime.strptime(date, '%Y-%m-%d')
                except ValueError:
                    errors['date'] = u"Enter the correct date format (Example: 2017-9-25)"
                else:
                    multitime['date'] = date

            # Start_time_1 validation:
            start_time_1 = request.POST.get('start_time_1')
            postdata['start_time_1'] = start_time_1
            if not start_time_1:
                errors['start_time_1'] = u"Please, enter the Start Time."
            else:
                try:
                    datetime.strptime(start_time_1, '%H:%M')
                except ValueError:
                    errors['start_time_1'] = u"Enter the correct time format (Example: 11:30)"
                else:
                    multitime['start_time_1'] = start_time_1

            # End_time_1 validation:
            end_time_1 = request.POST.get('end_time_1')
            postdata['end_time_1'] = end_time_1
            if not end_time_1:
                errors['end_time_1'] = u"Please, enter the Start Time."
            else:
                try:
                    datetime.strptime(end_time_1, '%H:%M')
                except ValueError:
                    errors['end_time_1'] = u"Enter the correct time format (Example: 12:00)"
                else:
                    multitime['end_time_1'] = end_time_1
            
            # IF Not Errors:
            if not errors:
                multidate = MultiTime(**multitime) # Create MultiTime object
                multidate.save() # Save MultiTime object in databse

                data['date1'] = MultiTime.objects.get(id=multidate.id) # add MultiTime object into data

                appointment = Appointment(**data) # Create Appointment object
                appointment.save() # Save appointment object in database

                # redirect to appointments list with success message:
                messages.success(request,'Created appointment %s successfully!' % appointment.title)
                return HttpResponseRedirect(reverse('appointments_list'))
            else:
                # return data with errors:
                return render(request, 'manager/appointments_add.html', {'errors':errors, 'postdata':postdata})

        # cancel button == PUSH:
        elif request.POST.get('cancel_button') is not None:
            # redirect to appointments list page with cancel message:
            messages.warning(request, 'Canceled appointment add!')
            return HttpResponseRedirect(reverse('appointments_list'))
    else:
        # initial Form
        return render(request,'manager/appointments_add.html',{})
