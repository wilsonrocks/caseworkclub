# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 08:11
from __future__ import unicode_literals

import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caseworkclub', '0002_auto_20170218_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='facility_time',
            field=models.BooleanField(verbose_name='Pays into facility time pot'),
        ),
        migrations.AlterField(
            model_name='jobtype',
            name='typename',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='membership_number',
            field=models.CharField(max_length=6, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='NUT Membership Numbers have a capital letter and five digits.', regex='[A-Z]\\d{5}')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(message='Phonenumber must be 11 digits long and start with 0', regex='0[0-9]{10}')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(message='Phonenumber must be 11 digits long and start with 0', regex='0[0-9]{10}')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]