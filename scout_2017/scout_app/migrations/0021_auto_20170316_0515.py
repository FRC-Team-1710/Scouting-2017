# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout_app', '0020_auto_20170316_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teleopdata',
            name='teleop_fuel_accuracy',
            field=models.IntegerField(default=0),
        ),
    ]