# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout_app', '0019_auto_20170316_0453'),
    ]

    operations = [
        migrations.AddField(
            model_name='teleopdata',
            name='dumper_bot',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teleopdata',
            name='floor_intake',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='autodata',
            name='auto_fuel_accuracy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='autodata',
            name='auto_fuel_speed',
            field=models.CharField(choices=[('did not attempt', 'did not attempt'), ('<1 ball/sec', '<1 ball/sec'), ('1 ball/sec', '1 ball/sec'), ('3 balls/sec', '3 balls/sec'), ('5+ balls/sec', '5+ balls/sec'), ('faster than the speed of light', 'faster than the speed of light')], default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='teleopdata',
            name='teleop_fuel_speed',
            field=models.CharField(choices=[('did not attempt', 'did not attempt'), ('<1 ball/sec', '<1 ball/sec'), ('1 ball/sec', '1 ball/sec'), ('3 balls/sec', '3 balls/sec'), ('5+ balls/sec', '5+ balls/sec'), ('faster than the speed of light', 'faster than the speed of light')], default=0, max_length=100),
        ),
    ]