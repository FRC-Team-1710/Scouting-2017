# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout_app', '0028_autodata_gear_attempted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autodata',
            name='gear_attempted',
            field=models.CharField(choices=[('unfilled', 'unfilled'), ('did not attempt', 'did not attempt'), ('pilot error', 'pilot error'), ('gear in bot', 'gear in bot'), ('missed the peg', 'missed the peg'), ('successfully placed', 'successfully placed')], max_length=100),
        ),
    ]
