# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('key_pass', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('ldap_password', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('group', models.ManyToManyField(to='UserManage.Group')),
            ],
        ),
    ]
