# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout_app', '0015_bet_claimed'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamdata',
            name='current_scout',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
