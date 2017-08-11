# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_submitdata_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='description',
            field=models.TextField(max_length=500, null=True, verbose_name='Description'),
            preserve_default=True,
        ),
    ]
