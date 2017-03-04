from django.contrib import admin
from .models import TeamData, AutoData, TeleopData, Scout, Bet

# Register your models here.

admin.site.register(TeamData)
admin.site.register(AutoData)
admin.site.register(TeleopData)
admin.site.register(Scout)
admin.site.register(Bet)
