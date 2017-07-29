# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_submitdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(max_length=100, null=True, verbose_name='Email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='submitdata',
            name='email',
            field=models.EmailField(max_length=100, null=True, verbose_name='Email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='submitdata',
            name='fullname',
            field=models.CharField(max_length=100, null=True, verbose_name='Full Name'),
            preserve_default=True,
        ),
    ]
