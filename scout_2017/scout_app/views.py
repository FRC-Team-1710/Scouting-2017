from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from scout_app.models import TeamData
from scout_app.forms import TeamInfoForm, AutoInfoForm, TeleopInfoForm

def index(request):
	return render(request, 'scout_app/index.html')

def scout_start(request):
	if request.method == 'POST':
        	form = TeamInfoForm(request.POST)
        	if form.is_valid():
            		form.save()
			return auto_input(request)
        	else:
        	    print form.errors
    	else:
        	form = TeamInfoForm()

	return render(request, 'scout_app/scout_start.html',{ 'form' : form})

def auto_input(request):
	if request.method == 'POST':
		form = AutoInfoForm(request.POST)
		if form.is_valid():
			form.save()
			return teleop_input(request)
		else:
			print form.errors
	else:
		form = AutoInfoForm(initial={'team_number' : TeamInfoForm.cleaned_data['team_number'],
					     'match_number' : TeamInfoForm.cleaned_data['match_number']})

	return render(request, 'scout_app/scout_auto.html', {'form' : form})

def teleop_input(request):
        if request.method == 'POST':
                form = TeleopInfoForm(request.POST)
                if form.is_valid():
                        form.save()
                        return index(request)
                else:
                        print form.errors
        else:
                form = TeleopInfoForm(initial={'team_number' : TeamInfoForm.cleaned_data['team_number'], 
                                             'match_number' : TeamInfoForm.cleaned_data['match_number']})

        return render(request, 'scout_app/scout_teleop.html', {'form' : form})


def view_data(request):
	latest_match_list = TeamData.objects.order_by('team_number')[:6]
	output = ', '.join(str([m.team_number for m in latest_match_list]))
	context = {'output' : output}
	return render(request, 'scout_app/view_data.html', context)
