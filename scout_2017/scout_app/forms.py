from django import forms
from scout_app.models import TeamData, TeleopData, AutoData
from scout_app.choices import *


class TeamInfoForm(forms.ModelForm):
	match_number = forms.IntegerField(help_text="enter Match Number",required=True)
	team_number = forms.IntegerField(help_text="enter team number",required=True)

	class Meta:
		model = TeamData
		fields = '__all__'

class AutoInfoForm(forms.ModelForm):
        match_number = forms.IntegerField(help_text="enter Match Number",required=True)
        team_number = forms.IntegerField(help_text="enter team number",required=True)
	
	baseline_crossed = forms.BooleanField(help_text="did your team cross the baseline?", required = False)
	auto_gears_placed = forms.IntegerField(help_text="how many gears were placed by your team in auto", widget=forms.Select(choices=GEAR_COUNTER), required = True)
	auto_fuel_accuracy = forms.IntegerField(help_text="How accurate is their shooter in auto?", widget=forms.Select(choices=ACCURACY_CHOICES), required = False)
	auto_fuel_speed = forms.IntegerField(help_text="How fast did your team shoot in auto", widget=forms.Select(choices=SPEED_CHOICES), required = False)
	hopper_efficiency = forms.IntegerField(help_text="How well were they able to retrieve hopper balls?", widget=forms.Select(choices=HOPPER_EFFICIENCY), required = False)
	

        class Meta:
                model = AutoData
                fields = '__all__'

class TeleopInfoForm(forms.ModelForm):
	match_number = forms.IntegerField(help_text="enter match number", required = True)
        team_number = forms.IntegerField(help_text="enter team number",required=True)

	gears_placed = forms.IntegerField(help_text="how many gears did your team place?", widget=forms.Select(choices=GEAR_COUNTER), required = True)
	teleop_fuel_accuracy = forms.IntegerField(help_text="How accurate is their shooter in teleop", widget=forms.Select(choices=ACCURACY_CHOICES), required = False)
	teleop_fuel_speed = forms.IntegerField(help_text="How fast is their shooter in teleop", widget=forms.Select(choices=SPEED_CHOICES), required = False)
	robot_speed = forms.CharField(help_text="How fast is their robot", widget=forms.Select(choices=ROBOT_SPEED), required = False)

	pilot_rating = forms.CharField(help_text="How well did their pilot perform", widget=forms.Select(choices=PILOT_RATING), required = False)
	climber_success = forms.CharField(help_text="Did their robot climb?", widget=forms.Select(choices=CLIMBER_SUCCESS), required = False)

        class Meta:
                model = TeleopData
                fields = '__all__'

class TeamLookupForm(forms.Form):
	team_number = forms.IntegerField(help_text="Team Lookup", required = True)
