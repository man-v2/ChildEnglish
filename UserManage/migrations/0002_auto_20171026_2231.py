# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserManage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='key_pass',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ldap_password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
