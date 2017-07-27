# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=266, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointment',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MultiTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(null=True, verbose_name=b'Date')),
                ('start_time_1', models.TimeField(null=True, verbose_name=b'Start Time #1')),
                ('end_time_1', models.TimeField(null=True, verbose_name=b'End Time #1')),
                ('start_time_2', models.TimeField(null=True, verbose_name=b'Start Time #2', blank=True)),
                ('end_time_2', models.TimeField(null=True, verbose_name=b'End Time #2', blank=True)),
                ('start_time_3', models.TimeField(null=True, verbose_name=b'Start Time #3', blank=True)),
                ('end_time_3', models.TimeField(null=True, verbose_name=b'End Time #3', blank=True)),
            ],
            options={
                'verbose_name': 'Multi Date',
                'verbose_name_plural': 'Multi Dates',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='appointment',
            name='date1',
            field=models.ForeignKey(related_name='date1', verbose_name='Date #1', to='manager.MultiTime', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='date2',
            field=models.ForeignKey(related_name='date2', verbose_name='Date #2', blank=True, to='manager.MultiTime', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='date3',
            field=models.ForeignKey(related_name='date3', verbose_name='Date #3', blank=True, to='manager.MultiTime', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='date4',
            field=models.ForeignKey(related_name='date4', verbose_name='Date #4', blank=True, to='manager.MultiTime', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='date5',
            field=models.ForeignKey(related_name='date5', verbose_name='Date #5', blank=True, to='manager.MultiTime', null=True),
            preserve_default=True,
        ),
    ]
