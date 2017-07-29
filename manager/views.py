from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from datetime import datetime
from validate_email import validate_email
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .models import Appointment, MultiTime, SubmitData

def appointments_list(request):
    ''' Appointments List method '''
    appointments = Appointment.objects.all()

    return render(request, 'manager/appointments_list.html', {'appointments':appointments})

def appointments_add(request):
    ''' Appointments Add method '''
    # POST == True
    if request.method == 'POST':
        # add button == PUSH:
        if request.POST.get('add_button') is not None:
            data = {} # data collection for Appointment
            errors = {} # erros collection

            # Validation data:

            # Title validation:
            title = request.POST.get('title')
            if not title:
                errors['title'] = u"Please, enter the Title"
            else:
                data['title'] = title

            # Date 1 validation:
            multitime = {} # data 1 collection for MultiTime
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
                errors['start_time_1'] = u"Please, enter the Start Time 1"
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
                errors['end_time_1'] = u"Please, enter the End Time 2"
            else:
                try:
                    datetime.strptime(end_time_1, '%H:%M')
                except ValueError:
                    errors['end_time_1'] = u"Enter the correct time format (Example: 12:00)"
                else:
                    multitime['end_time_1'] = end_time_1

            # Start and End Time 2 validation:
            start_time_2 = request.POST.get('start_time_2')
            end_time_2 = request.POST.get('end_time_2')
            if not start_time_2 and not end_time_2:
                pass
            elif not start_time_2 or not end_time_2:
                if not start_time_2:
                    errors['start_time_2'] = u"Enter Start Time 2"
                elif not end_time_2:
                    errors['end_time_2'] = u"Enter End Time 2"
            elif start_time_2 and end_time_2:
                try:
                    datetime.strptime(start_time_2, '%H:%M')
                except ValueError:
                    errors['start_time_2'] = u"Enter the correct time format (Example: 12:00)"
                else:
                    multitime['start_time_2'] = start_time_2
                try:
                    datetime.strptime(end_time_2, '%H:%M')
                except ValueError:
                    errors['end_time_2'] = u"Enter the correct time format (Example: 12:00)"
                else:
                    multitime['end_time_2'] = end_time_2

            # Start and End Time 3 validation:
            start_time_3 = request.POST.get('start_time_3')
            end_time_3 = request.POST.get('end_time_3')
            if not start_time_3 and not end_time_3:
                pass
            elif not start_time_3 or not end_time_3:
                if not start_time_3:
                    errors['start_time_3'] = u"Enter Start Time 3"
                elif not end_time_3:
                    errors['end_time_3'] = u"Enter End Time 3"
            elif start_time_3 and end_time_3:
                try:
                    datetime.strptime(start_time_3, '%H:%M')
                except ValueError:
                    errors['start_time_3'] = u"Enter the correct time format (Example: 12:00)"
                else:
                    multitime['start_time_3'] = start_time_3
                try:
                    datetime.strptime(end_time_3, '%H:%M')
                except ValueError:
                    errors['end_time_3'] = u"Enter the correct time format (Example: 12:00)"
                else:
                    multitime['end_time_3'] = end_time_3

            # Date 2 validation:
            multitime2 = {} # data 2 collection for MultiTime
            # Date validation:
            date2 = request.POST.get('date2')
            if not date2:
                pass
            else:
                try:
                    datetime.strptime(date2, '%Y-%m-%d')
                except ValueError:
                    errors['date2'] = u"Enter the correct date format (Example: 2017-9-25)"
                else:
                    multitime2['date'] = date2

            if date2:
                # Start_time_1 validation:
                d2_start_time_1 = request.POST.get('d2_start_time_1')
                if not d2_start_time_1:
                    errors['d2_start_time_1'] = u"Please, enter the Start Time 1"
                else:
                    try:
                        datetime.strptime(d2_start_time_1, '%H:%M')
                    except ValueError:
                        errors['d2_start_time_1'] = u"Enter the correct time format (Example: 11:30)"
                    else:
                        multitime2['start_time_1'] = d2_start_time_1

                # End_time_1 validation:
                d2_end_time_1 = request.POST.get('d2_end_time_1')
                if not d2_end_time_1:
                    errors['d2_end_time_1'] = u"Please, enter the End Time 2"
                else:
                    try:
                        datetime.strptime(d2_end_time_1, '%H:%M')
                    except ValueError:
                        errors['d2_end_time_1'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime2['end_time_1'] = d2_end_time_1

                # Start and End Time 2 validation:
                d2_start_time_2 = request.POST.get('d2_start_time_2')
                d2_end_time_2 = request.POST.get('d2_end_time_2')
                if not d2_start_time_2 and not d2_end_time_2:
                    pass
                elif not d2_start_time_2 or not d2_end_time_2:
                    if not d2_start_time_2:
                        errors['d2_start_time_2'] = u"Enter Start Time 2"
                    elif not d2_end_time_2:
                        errors['d2_end_time_2'] = u"Enter End Time 2"
                elif d2_start_time_2 and d2_end_time_2:
                    try:
                        datetime.strptime(d2_start_time_2, '%H:%M')
                    except ValueError:
                        errors['d2_start_time_2'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime2['start_time_2'] = d2_start_time_2
                    try:
                        datetime.strptime(d2_end_time_2, '%H:%M')
                    except ValueError:
                        errors['d2_end_time_2'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime2['end_time_2'] = d2_end_time_2

                # Start and End Time 3 validation:
                d2_start_time_3 = request.POST.get('d2_start_time_3')
                d2_end_time_3 = request.POST.get('d2_end_time_3')
                if not d2_start_time_3 and not d2_end_time_3:
                    pass
                elif not d2_start_time_3 or not d2_end_time_3:
                    if not d2_start_time_3:
                        errors['d2_start_time_3'] = u"Enter Start Time 3"
                    elif not d2_end_time_3:
                        errors['d2_end_time_3'] = u"Enter End Time 3"
                elif d2_start_time_3 and d2_end_time_3:
                    try:
                        datetime.strptime(d2_start_time_3, '%H:%M')
                    except ValueError:
                        errors['d2_start_time_3'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime2['start_time_3'] = d2_start_time_3
                    try:
                        datetime.strptime(d2_end_time_3, '%H:%M')
                    except ValueError:
                        errors['d2_end_time_3'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime2['end_time_3'] = d2_end_time_3
            else:
                pass

            # Date 3 validation:
            multitime3 = {} # data 3 collection for MultiTime
            # Date validation:
            date3 = request.POST.get('date3')
            if not date3:
                pass
            else:
                try:
                    datetime.strptime(date3, '%Y-%m-%d')
                except ValueError:
                    errors['date3'] = u"Enter the correct date format (Example: 2017-9-25)"
                else:
                    multitime3['date'] = date3

            if date3:
                # Start_time_1 validation:
                d3_start_time_1 = request.POST.get('d3_start_time_1')
                if not d3_start_time_1:
                    errors['d3_start_time_1'] = u"Please, enter the Start Time 1"
                else:
                    try:
                        datetime.strptime(d3_start_time_1, '%H:%M')
                    except ValueError:
                        errors['d3_start_time_1'] = u"Enter the correct time format (Example: 11:30)"
                    else:
                        multitime3['start_time_1'] = d3_start_time_1

                # End_time_1 validation:
                d3_end_time_1 = request.POST.get('d3_end_time_1')
                if not d3_end_time_1:
                    errors['d3_end_time_1'] = u"Please, enter the End Time 2"
                else:
                    try:
                        datetime.strptime(d3_end_time_1, '%H:%M')
                    except ValueError:
                        errors['d3_end_time_1'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime3['end_time_1'] = d3_end_time_1

                # Start and End Time 2 validation:
                d3_start_time_2 = request.POST.get('d3_start_time_2')
                d3_end_time_2 = request.POST.get('d3_end_time_2')
                if not d3_start_time_2 and not d3_end_time_2:
                    pass
                elif not d3_start_time_2 or not d3_end_time_2:
                    if not d3_start_time_2:
                        errors['d3_start_time_2'] = u"Enter Start Time 2"
                    elif not d3_end_time_2:
                        errors['d3_end_time_2'] = u"Enter End Time 2"
                elif d3_start_time_2 and d3_end_time_2:
                    try:
                        datetime.strptime(d3_start_time_2, '%H:%M')
                    except ValueError:
                        errors['d3_start_time_2'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime3['start_time_2'] = d3_start_time_2
                    try:
                        datetime.strptime(d3_end_time_2, '%H:%M')
                    except ValueError:
                        errors['d3_end_time_2'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime2['end_time_2'] = d3_end_time_2

                # Start and End Time 3 validation:
                d3_start_time_3 = request.POST.get('d3_start_time_3')
                d3_end_time_3 = request.POST.get('d3_end_time_3')
                if not d3_start_time_3 and not d3_end_time_3:
                    pass
                elif not d3_start_time_3 or not d3_end_time_3:
                    if not d3_start_time_3:
                        errors['d3_start_time_3'] = u"Enter Start Time 3"
                    elif not d3_end_time_3:
                        errors['d3_end_time_3'] = u"Enter End Time 3"
                elif d3_start_time_3 and d3_end_time_3:
                    try:
                        datetime.strptime(d3_start_time_3, '%H:%M')
                    except ValueError:
                        errors['d3_start_time_3'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime3['start_time_3'] = d3_start_time_3
                    try:
                        datetime.strptime(d3_end_time_3, '%H:%M')
                    except ValueError:
                        errors['d3_end_time_3'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime3['end_time_3'] = d3_end_time_3
            else:
                pass

            # Date 4 validation:
            multitime4 = {} # data 4 collection for MultiTime
            # Date validation:
            date4 = request.POST.get('date4')
            if not date4:
                pass
            else:
                try:
                    datetime.strptime(date4, '%Y-%m-%d')
                except ValueError:
                    errors['date4'] = u"Enter the correct date format (Example: 2017-9-25)"
                else:
                    multitime4['date'] = date4

            if date4:
                # Start_time_1 validation:
                d4_start_time_1 = request.POST.get('d4_start_time_1')
                if not d4_start_time_1:
                    errors['d4_start_time_1'] = u"Please, enter the Start Time 1"
                else:
                    try:
                        datetime.strptime(d4_start_time_1, '%H:%M')
                    except ValueError:
                        errors['d4_start_time_1'] = u"Enter the correct time format (Example: 11:30)"
                    else:
                        multitime4['start_time_1'] = d4_start_time_1

                # End_time_1 validation:
                d4_end_time_1 = request.POST.get('d4_end_time_1')
                if not d4_end_time_1:
                    errors['d4_end_time_1'] = u"Please, enter the End Time 2"
                else:
                    try:
                        datetime.strptime(d4_end_time_1, '%H:%M')
                    except ValueError:
                        errors['d4_end_time_1'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime4['end_time_1'] = d4_end_time_1

                # Start and End Time 2 validation:
                d4_start_time_2 = request.POST.get('d4_start_time_2')
                d4_end_time_2 = request.POST.get('d4_end_time_2')
                if not d4_start_time_2 and not d4_end_time_2:
                    pass
                elif not d4_start_time_2 or not d4_end_time_2:
                    if not d4_start_time_2:
                        errors['d4_start_time_2'] = u"Enter Start Time 2"
                    elif not d4_end_time_2:
                        errors['d4_end_time_2'] = u"Enter End Time 2"
                elif d4_start_time_2 and d4_end_time_2:
                    try:
                        datetime.strptime(d4_start_time_2, '%H:%M')
                    except ValueError:
                        errors['d4_start_time_2'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime4['start_time_2'] = d4_start_time_2
                    try:
                        datetime.strptime(d4_end_time_2, '%H:%M')
                    except ValueError:
                        errors['d4_end_time_2'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime4['end_time_2'] = d4_end_time_2

                # Start and End Time 3 validation:
                d4_start_time_3 = request.POST.get('d4_start_time_3')
                d4_end_time_3 = request.POST.get('d4_end_time_3')
                if not d4_start_time_3 and not d4_end_time_3:
                    pass
                elif not d4_start_time_3 or not d4_end_time_3:
                    if not d4_start_time_3:
                        errors['d4_start_time_3'] = u"Enter Start Time 3"
                    elif not d4_end_time_3:
                        errors['d4_end_time_3'] = u"Enter End Time 3"
                elif d4_start_time_3 and d4_end_time_3:
                    try:
                        datetime.strptime(d4_start_time_3, '%H:%M')
                    except ValueError:
                        errors['d4_start_time_3'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime4['start_time_3'] = d4_start_time_3
                    try:
                        datetime.strptime(d4_end_time_3, '%H:%M')
                    except ValueError:
                        errors['d4_end_time_3'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime4['end_time_3'] = d4_end_time_3
            else:
                pass

            # Date 5 validation:
            multitime5 = {} # data 5 collection for MultiTime
            # Date validation:
            date5 = request.POST.get('date5')
            if not date5:
                pass
            else:
                try:
                    datetime.strptime(date5, '%Y-%m-%d')
                except ValueError:
                    errors['date5'] = u"Enter the correct date format (Example: 2017-9-25)"
                else:
                    multitime5['date'] = date5

            if date5:
                # Start_time_1 validation:
                d5_start_time_1 = request.POST.get('d5_start_time_1')
                if not d5_start_time_1:
                    errors['d5_start_time_1'] = u"Please, enter the Start Time 1"
                else:
                    try:
                        datetime.strptime(d5_start_time_1, '%H:%M')
                    except ValueError:
                        errors['d5_start_time_1'] = u"Enter the correct time format (Example: 11:30)"
                    else:
                        multitime5['start_time_1'] = d5_start_time_1

                # End_time_1 validation:
                d5_end_time_1 = request.POST.get('d5_end_time_1')
                if not d5_end_time_1:
                    errors['d5_end_time_1'] = u"Please, enter the End Time 2"
                else:
                    try:
                        datetime.strptime(d5_end_time_1, '%H:%M')
                    except ValueError:
                        errors['d5_end_time_1'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime5['end_time_1'] = d5_end_time_1

                # Start and End Time 2 validation:
                d5_start_time_2 = request.POST.get('d5_start_time_2')
                d5_end_time_2 = request.POST.get('d5_end_time_2')
                if not d5_start_time_2 and not d5_end_time_2:
                    pass
                elif not d5_start_time_2 or not d5_end_time_2:
                    if not d5_start_time_2:
                        errors['d5_start_time_2'] = u"Enter Start Time 2"
                    elif not d5_end_time_2:
                        errors['d5_end_time_2'] = u"Enter End Time 2"
                elif d5_start_time_2 and d5_end_time_2:
                    try:
                        datetime.strptime(d5_start_time_2, '%H:%M')
                    except ValueError:
                        errors['d5_start_time_2'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime5['start_time_2'] = d5_start_time_2
                    try:
                        datetime.strptime(d5_end_time_2, '%H:%M')
                    except ValueError:
                        errors['d5_end_time_2'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime5['end_time_2'] = d5_end_time_2

                # Start and End Time 3 validation:
                d5_start_time_3 = request.POST.get('d5_start_time_3')
                d5_end_time_3 = request.POST.get('d5_end_time_3')
                if not d5_start_time_3 and not d5_end_time_3:
                    pass
                elif not d5_start_time_3 or not d5_end_time_3:
                    if not d5_start_time_3:
                        errors['d5_start_time_3'] = u"Enter Start Time 3"
                    elif not d5_end_time_3:
                        errors['d5_end_time_3'] = u"Enter End Time 3"
                elif d5_start_time_3 and d5_end_time_3:
                    try:
                        datetime.strptime(d5_start_time_3, '%H:%M')
                    except ValueError:
                        errors['d5_start_time_3'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime5['start_time_3'] = d5_start_time_3
                    try:
                        datetime.strptime(d5_end_time_3, '%H:%M')
                    except ValueError:
                        errors['d5_end_time_3'] = u"Enter the correct time format (Example: 12:00)"
                    else:
                        multitime5['end_time_3'] = d5_end_time_3
            else:
                pass

            # IF Not Errors:
            if not errors:
                multidate = MultiTime(**multitime) # Create MultiTime object
                multidate.save() # Save MultiTime object in databse

                data['date1'] = MultiTime.objects.get(id=multidate.id) # add MultiTime object into data

                if date2:
                    multidate2 = MultiTime(**multitime2)
                    multidate2.save()
                    data['date2'] = MultiTime.objects.get(id=multidate2.id)
                else:
                    pass

                if date3:
                    multidate3 = MultiTime(**multitime3)
                    multidate3.save()
                    data['date3'] = MultiTime.objects.get(id=multidate3.id)
                else:
                    pass

                if date4:
                    multidate4 = MultiTime(**multitime4)
                    multidate4.save()
                    data['date4'] = MultiTime.objects.get(id=multidate4.id)
                else:
                    pass

                if date5:
                    multidate5 = MultiTime(**multitime5)
                    multidate5.save()
                    data['date5'] = MultiTime.objects.get(id=multidate5.id)
                else:
                    pass

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
            if len(time) == 13:
                for index, element in enumerate(str(time)):
                  if index == 0:
                      t_id.append(element) # save id
                  elif index in [2,3,4,5,6]:
                      time_s.append(element) # save start time
                  elif index in [8,9,10,11,12]:
                      time_e.append(element) # save end time
            elif len(time) == 14:
                for index, element in enumerate(str(time)):
                  if index in [0,1]:
                      t_id.append(element) # save id
                  elif index in [3,4,5,6,7]:
                      time_s.append(element) # save start time
                  elif index in [9,10,11,12,13]:
                      time_e.append(element) # save end time
            elif len(time) == 15:
                for index, element in enumerate(str(time)):
                  if index in [0,1,2]:
                      t_id.append(element) # save id
                  elif index in [4,5,6,7,8]:
                      time_s.append(element) # save start time
                  elif index in [10,11,12,13,14]:
                      time_e.append(element) # save end time
            multitime_id = ''.join(t_id) # convert id to int
            start_time = ''.join(time_s) # Strart Time final variable
            end_time = ''.join(time_e) # End Time final variable
            multitime = MultiTime.objects.get(id=multitime_id) # get MultiTime object
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
                data['date'] = multitime

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

        # Get title data:
        title = Appointment.objects.get(id=appointment.id)
        data['title'] = title

        # Errors == False:
        if not errors:
            # create SubmitData object:
            submit_data = SubmitData(**data)
            # save object in database:
            submit_data.save()
            # redirect to appointments list with success message:
            messages.success(request,'Success Submit Appointment!!')
            return HttpResponseRedirect(reverse('appointments_list'))
        else:
            # return form with errros and save input data:
            return render(request, 'manager/appointments_form.html', {'aid':aid, 'appointment':appointment, 'errors':errors, 'postdata': postadata})
    elif request.POST.get('cancel_button') is not None:
        # redirect to appointments list with cancel message:
        messages.warning(request,"Cancel Submit Appointment!")
        return HttpResponseRedirect(reverse('appointments_list'))
    else:
        return render(request, 'manager/appointments_form.html', {'aid':aid, 'appointment':appointment})

def submit_data_list(request):
    ''' Submit Data list of Appointments Form '''
    submit_data_list = SubmitData.objects.all().order_by('date')

    return render(request,'manager/submit_data_list.html',{'submit_data_list': submit_data_list })

def authentication(request):
    ''' Authentication User method '''
    # Add Button == PUSH
    if request.POST.get('add_button') is not None:
        # help variables:
        data = {} # data collection
        errors = {} # errors collection
        # GET DATA:
        username = request.POST.get('name') # get name
        email = request.POST.get('email') # get email
        # name validation:
        if not username:
            errors['name'] = u"Enter Name, please!"
        # email validation:
        if not email:
            errors['email'] = u"Enter Email, please!"
        else:
            email_valid = validate_email(email)
            if email_valid == False:
                errors['email'] = u"Enter correct Email, please!"
        # Errors == False
        if not errors:
            # Authentication Data:
            authentication = authenticate(username=username,email=email,password='1')
            # Authentication == True:
            if authentication is not None:
                user = User.objects.get(username=username) # get user from data base
                # Authentication Email == User Email:
                if user.email == email:
                    # Log in user:
                    login(request,authentication)
                    # refirect to appointments list with success message:
                    messages.success(request,'You are authenticated!')
                    return HttpResponseRedirect(reverse('appointments_list'))
                # Authentication Email != User Email:
                else:
                    # redirect to appointments list with errors and input data:
                    errors['email'] = u"It's not email from this name, enter correct email, please!"
                    return render(request, 'manager/authentication.html', {'errors':errors})
            # Authentication == False:
            else:
                # Create new user in database:
                user = User.objects.create_user(username,email,'1')
                user.save() # save this user
                # Repeated Authentication
                authentication = authenticate(username=username,email=email,password='1')
                # Log in user:
                login(request,authentication)
                # redirect to appointments list with success message:
                messages.success(request,'You are authenticated!')
                return HttpResponseRedirect(reverse('appointments_list'))
        # Errros == True
        else:
            # return errors and user input data:
            return render(request, 'manager/authentication.html', {'errors':errors})
    # Cancel Button == PUSH
    elif request.POST.get('cancel'):
        # redirect to appointments list wit cancel message:
        messages.warning(request,'Sign in canceled!') # cancel message
        return HttpResponseRedirect(reverse('appointments_list'))
    else:
        # inital Sign in Form
        return render(request, 'manager/authentication.html', {})
