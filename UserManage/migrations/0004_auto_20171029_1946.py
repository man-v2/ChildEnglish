# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 11:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('UserManage', '0003_auto_20171026_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default=datetime.datetime(2017, 10, 29, 11, 45, 16, 337172, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default=datetime.datetime(2017, 10, 29, 11, 45, 39, 467918, tzinfo=utc), max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
