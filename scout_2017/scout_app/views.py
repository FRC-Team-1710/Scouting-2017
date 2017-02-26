from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from scout_app.models import TeamData
from scout_app.forms import BasicInfoForm

def index(request):
	return render(request, 'scout_app/index.html')

def scout_start(request):
	if request.method == 'POST':
        	form = BasicInfoForm(request.POST)
        	if form.is_valid():
            		form.save()
			team_number = form.cleaned_data.get('team_number')
            		return auto_input(request, team_number)
        	else:
        	    print form.errors
    	else:
        	form = BasicInfoForm()

	return render(request, 'scout_app/scout_start.html',{ 'form' : form })

def auto_input(request, team_number):
	if request.method == 'POST':
		form = AutonomousInfoForm(request.POST)
		if form.is_valid():
			form.save()
			return teleop_input(request)
		else:
			print form.errors
	else:
		form = AutonomousInfoForm()

	return render(request, 'scout_app/auto_scout.html', {'team_number' : team_number})

def teleop_input(request):
	return render(request, 'scout_app/teleop_scout.html')
