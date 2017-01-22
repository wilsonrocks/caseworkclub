# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-21 20:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caseworkclub', '0006_auto_20170121_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='caseworker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.Caseworker'),
        ),
        migrations.AlterField(
            model_name='case',
            name='workplace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.Workplace'),
        ),
    ]
