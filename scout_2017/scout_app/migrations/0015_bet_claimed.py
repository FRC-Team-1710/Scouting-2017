# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout_app', '0014_auto_20170305_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='claimed',
            field=models.BooleanField(default=False),
        ),
    ]
