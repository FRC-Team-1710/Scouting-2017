from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TeamData(models.Model):
	match_number = models.PositiveIntegerField(default = 0)
	team_number = models.PositiveIntegerField(default = 0000)

	baseline_cross = models.BooleanField(default = False)
