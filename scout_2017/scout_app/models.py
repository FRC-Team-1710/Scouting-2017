from __future__ import unicode_literals

from django.db import models

from scout_app.choices import *


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class TeamData(models.Model):
	match_number = models.PositiveIntegerField(default = 0)
	team_number = models.PositiveIntegerField(default = 0000)
	alliance_color = models.CharField(choices=ALLIANCE_COLORS, max_length=100, default=0)
	current_scout = models.CharField(max_length=100, default = 0)

class AutoData(models.Model):
	match_number = models.PositiveIntegerField(default = 0)
	team_number = models.PositiveIntegerField(default = 0)
	baseline_crossed = models.BooleanField(default=False)
	auto_gears_placed = models.IntegerField(choices=GEAR_COUNTER, default = 0)
	auto_fuel_accuracy = models.IntegerField(choices=ACCURACY_CHOICES, default = 0)
	auto_fuel_speed = models.IntegerField(choices=SPEED_CHOICES, default = 0)
	hopper_efficiency = models.IntegerField(choices=HOPPER_EFFICIENCY, default = 0)

class TeleopData(models.Model):
	match_number = models.PositiveIntegerField(default = 0)
	team_number = models.PositiveIntegerField(default = 0)
	gears_placed = models.IntegerField(choices=GEAR_COUNTER, default = 0)
	teleop_fuel_accuracy = models.IntegerField(choices=ACCURACY_CHOICES, default = 0)
	teleop_fuel_speed = models.PositiveIntegerField(choices=SPEED_CHOICES, default = 0)
	robot_speed = models.CharField(choices=ROBOT_SPEED, max_length = 100, default = 0)
	pilot_rating = models.CharField(choices=PILOT_RATING, max_length = 100, default = 0)
	climber_success = models.CharField(choices=CLIMBER_SUCCESS, max_length = 100, default = 0)
	winning_alliance = models.CharField(choices=ALLIANCE_COLORS, max_length = 100, default = 0)

class Scout(models.Model):
	user = models.CharField(max_length = 100, default = 0)
	scout_sheckles = models.IntegerField(default = 100)

class BetHandler(models.Model):
	money_in_pot = models.IntegerField(default = 0)
	match_number = models.PositiveIntegerField(default = 0)
	winning_alliance = models.CharField(default=0, max_length=100)

class Bet(models.Model):
	user = models.CharField(default=0, max_length=100)
	match_number = models.IntegerField(default = 0)
	alliance_bet_on = models.CharField(default=0, max_length=100)
	money_bet = models.IntegerField(default = 0)
	claimed = models.BooleanField(default=False)
