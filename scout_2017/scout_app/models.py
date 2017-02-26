from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TeamData(models.Model):
	match_number = models.PositiveIntegerField(default = 0)
	team_number = models.PositiveIntegerField(default = 0000)

class AutoData(models.Model):
	match_number = models.PositiveIntegerField(default = 0)
	team_number = models.PositiveIntegerField(default = 0)
	baseline_crossed = models.BooleanField(default=False)

class TeleopData(models.Model):
	match_number = models.PositiveIntegerField(default = 0)
	team_number = models.PositiveIntegerField(default = 0)
	gears_placed = models.PositiveIntegerField(default = 0)
