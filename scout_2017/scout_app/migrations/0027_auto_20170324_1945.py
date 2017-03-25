# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout_app', '0026_teams'),
    ]

    operations = [
        migrations.AddField(
            model_name='autodata',
            name='peg_placed_on',
            field=models.CharField(choices=[('unfilled', 'unfilled'), ('did not attempt', 'did not attempt'), ('left peg', 'left peg'), ('center peg', 'center peg'), ('right peg', 'right peg')], default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='teleopdata',
            name='climber_success',
            field=models.CharField(choices=[('unfilled', 'unfilled'), ('did not attempt', 'did not attempt'), ('did not press button', 'did not press button'), ('fell off rope', 'fell off rope'), ('rope snapped', 'rope snapped'), ('climbed successfully', 'climbed successfully')], default=0, max_length=100),
        ),
    ]