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
	auto_fuel_accuracy = forms.IntegerField(help_text="How accurate is their shooter in auto?", required = False)

        class Meta:
                model = AutoData
                fields = '__all__'

class TeleopInfoForm(forms.ModelForm):
	match_number = forms.IntegerField(help_text="enter match number", required = True)
        team_number = forms.IntegerField(help_text="enter team number",required=True)

	gears_placed = forms.IntegerField(help_text="how many gears did your team place?", required = False)

        class Meta:
                model = TeleopData
                fields = '__all__'

class TeamLookupForm(forms.Form):
	team_number = forms.IntegerField(help_text="Team Lookup", required = True)
