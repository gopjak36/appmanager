from django.db import models

class MultiTime(models.Model):
    ''' Multi Time for Appontment '''

    class Meta:
        verbose_name = "Multi Date"
        verbose_name_plural = "Multi Dates"

    date = models.DateField(
                blank=False,
                null=True,
                verbose_name='Date')


    def __unicode__(self):
        return u"%s" % (self.date)

# Avaliable time for date:
for num in range(1,4):
    if num == 1:
        MultiTime.add_to_class('start_time_'+str(num), models.TimeField(blank=False, null=True, verbose_name="Start Time #"+str(num)))
        MultiTime.add_to_class('end_time_'+str(num), models.TimeField(blank=False, null=True, verbose_name="End Time #"+str(num)))
    else:
        MultiTime.add_to_class('start_time_'+str(num), models.TimeField(blank=True, null=True, verbose_name="Start Time #"+str(num)))
        MultiTime.add_to_class('end_time_'+str(num), models.TimeField(blank=True, null=True, verbose_name="End Time #"+str(num)))


class Appointment(models.Model):
    ''' Appointmant '''

    class Meta:
        verbose_name = u"Appointment"
        verbose_name_plural = u"Appointment"

    title = models.CharField(
                max_length=266,
                blank=False,
                null=True,
                verbose_name=u"Title")

    def __unicode__(self):
        return u"%s" % self.title

# Avaliable date for Appointment:
for num in range(1,6):
    if num == 1:
        Appointment.add_to_class('date'+str(num), models.ForeignKey('MultiTime', blank=False, null=True ,related_name=u"date"+str(num), verbose_name=u"Date #"+str(num)))
    else:
        Appointment.add_to_class('date'+str(num), models.ForeignKey('MultiTime', blank=True, null=True ,related_name=u"date"+str(num), verbose_name=u"Date #"+str(num)))
