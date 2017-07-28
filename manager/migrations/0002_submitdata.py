# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.CharField(max_length=5, null=True, verbose_name='Start Time')),
                ('end_time', models.CharField(max_length=5, null=True, verbose_name='End Time')),
                ('fullname', models.CharField(max_length=100, null=True, verbose_name='End Time')),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='Email Time')),
                ('date', models.ForeignKey(verbose_name='Date', to='manager.MultiTime', null=True)),
                ('title', models.ForeignKey(verbose_name='Title', to='manager.Appointment', null=True)),
            ],
            options={
                'verbose_name': 'Submit Data',
                'verbose_name_plural': 'Submit Datas',
            },
            bases=(models.Model,),
        ),
    ]
