from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    # List Appointments url:
    url(r'^$', 'manager.views.appointments_list', name="appointments_list"),

    # List Appointments url:
    url(r'^add/$', 'manager.views.appointments_add', name="appointments_add"),

    # Admin Panel url:
    url(r'^admin/', include(admin.site.urls)),
)
