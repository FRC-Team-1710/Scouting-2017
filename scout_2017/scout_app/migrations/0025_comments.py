# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout_app', '0024_auto_20170317_0639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scout', models.CharField(default=0, max_length=100)),
                ('team_number', models.IntegerField(default=0)),
                ('comment', models.CharField(default=0, max_length=1200)),
            ],
        ),
    ]
