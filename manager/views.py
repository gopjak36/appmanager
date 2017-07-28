from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from datetime import datetime
from validate_email import validate_email

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

            # Validation data:

            # Title validation:
            title = request.POST.get('title')
            if not title:
                errors['title'] = u"Please, enter the Title"
            else:
                data['title'] = title

            # Date validation:
            date = request.POST.get('date')
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
                return render(request, 'manager/appointments_add.html', {'errors':errors})

        # cancel button == PUSH:
        elif request.POST.get('cancel_button') is not None:
            # redirect to appointments list page with cancel message:
            messages.warning(request, 'Canceled Appointment Add!')
            return HttpResponseRedirect(reverse('appointments_list'))
    else:
        # initial Form
        return render(request,'manager/appointments_add.html',{})

def appointments_form(request, aid):
    ''' Appointments Form method '''
    appointment = Appointment.objects.get(id=aid)
    if request.POST.get('add_button') is not None:
        data = {} # data collection
        errors = {} # errors collection
        postadata = {} # post data colelction

        # VALIDATION DATA

        # Time validation:
        time = request.POST.get('time') # value time from radion input
        postadata['time'] = time
        if not time:
            errors['time'] = u"Please, select Time"
        else:
            # GET DATA FROM VALUE
            # help variables:
            t_id = [] # MultiTime id
            time_s = [] # Start Time
            time_e = [] # End Time
            # Go over value as enumerate string:
            for index, element in enumerate(str(time)):
              if index == 0:
                  t_id.append(element) # save id
              elif index in [2,3,4,5,6]:
                  time_s.append(element) # save start time
              elif index in [8,9,10,11,12]:
                  time_e.append(element) # save end time
            multitime_id = ''.join(t_id) # convert id to int
            start_time = ''.join(time_s) # Strart Time final variable
            end_time = ''.join(time_e) # End Time final variable
            multitime = MultiTime.objects.get(id=multitime_id) # get MultiTime object

            data['time'] = multitime
            data['start_time'] = start_time
            data['end_time'] = end_time

        # Data validation:
        date = request.POST.get('date')
        postadata['date'] = date
        if not date:
            errors['date'] = u"Please, select Date"
        elif not time:
                errors['time'] = u"Please, select Time"
        else:
            if date != multitime_id:
                errors['date'] = u"Please, slect correct Date and Time "
            else:
                data['date'] = date

        # Full Name Validation:
        fullname = request.POST.get('fullname')
        if not fullname:
            errors['fullname'] = u"Please, write your Full Name"
        else:
            data['fullname'] = fullname

        # Email Validation
        email = request.POST.get('email')
        email_data = email
        if not email:
            errors['email'] = u"Please, write you Email"
        else:
            is_valid = validate_email(email)
            if is_valid == True:
                data['email'] = email
            else:
                errors['email'] = u"Please, write correct Email"

        return render(request, 'manager/appointments_form.html', {'aid':aid, 'appointment':appointment, 'errors':errors, 'postdata': postadata})
    elif request.POST.get('cancel_button') is not None:
        # redirect to appointments list with cancel message:
        messages.warning(request,"Cancel Submit Appointment!")
        return HttpResponseRedirect(reverse('appointments_list'))
    else:
        return render(request, 'manager/appointments_form.html', {'aid':aid, 'appointment':appointment})
