from __future__ import unicode_literals

from django.db import models

from scout_app.choices import *

# Create your models here.

class TeamData(models.Model):
	match_number = models.PositiveIntegerField(default = 0)
	team_number = models.PositiveIntegerField(default = 0000)

class AutoData(models.Model):
	match_number = models.PositiveIntegerField(default = 0)
	team_number = models.PositiveIntegerField(default = 0)
	baseline_crossed = models.BooleanField(default=False)
	gears_placed = models.PositiveIntegerField(default = 0)
	auto_fuel_accuracy = models.PositiveIntegerField(default = 0)
	auto_fuel_speed = models.PositiveIntegerField(default = 0)
	hopper_efficiency = models.PositiveIntegerField(default = 0)
	test_choice = models.IntegerField(choices=QUALITY_CHOICES, default = 1)

class TeleopData(models.Model):
	match_number = models.PositiveIntegerField(default = 0)
	team_number = models.PositiveIntegerField(default = 0)
	gears_placed = models.PositiveIntegerField(default = 0)
	teleop_fuel_accuracy = models.PositiveIntegerField(default = 0)
	teleop_fuel_speed = models.PositiveIntegerField(default = 0)
	fuel_floor_intake = models.BooleanField(default = False)
	
