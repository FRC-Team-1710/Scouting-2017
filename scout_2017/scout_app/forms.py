from django import forms
from scout_app.models import TeamData

class BasicInfoForm(forms.ModelForm):
	match_number = forms.IntegerField(help_text="enter Match Number",required=True)
	team_number = forms.IntegerField(help_text="enter team number",required=True)

	class Meta:
	        model = TeamData
		fields = '__all__'

class AutonomousInfoForm(forms.ModelForm):
	baseline_cross = forms.BooleanField(help_text="Did your team cross the baseline?", required=True)

	class Meta:
		model = TeamData
		fields = '__all__'
