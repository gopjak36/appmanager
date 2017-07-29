from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    # List Appointments url:
    url(r'^$', 'manager.views.appointments_list', name="appointments_list"),

    # List Appointments url:
    url(r'^add/$', 'manager.views.appointments_add', name="appointments_add"),

    # Form Appointments url:
    url(r'^(?P<aid>\d+)/form/$', 'manager.views.appointments_form', name="appointments_form"),

    # List of Submit Data from From Appointments url:
    url(r'^submitdata/$', 'manager.views.submit_data_list', name="submit_data_list"),

    # List Authentication url:
    url(r'^auth/$', 'manager.views.authentication', name="auth"),

    # Logout url:
     url(r'^logout/$', 'django.contrib.auth.views.logout',  {'next_page': '/'}, name='logout'),

    # Admin Panel url:
    url(r'^admin/', include(admin.site.urls)),
)
