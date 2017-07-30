# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20170729_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitdata',
            name='author',
            field=models.EmailField(max_length=100, null=True, verbose_name='Author'),
            preserve_default=True,
        ),
    ]
