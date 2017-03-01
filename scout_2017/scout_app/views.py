from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from scout_app.models import TeamData, AutoData, TeleopData, BetHandler
from scout_app.forms import TeamInfoForm, AutoInfoForm, TeleopInfoForm, TeamLookupForm, PlaceBetForm, ScoutRegister, ScoutLogin

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def index(request):
	return render(request, 'scout_app/index.html')

def scout_register(request):
	if request.method == 'POST':
		form = ScoutRegister(request.POST)
		if form.is_valid():
			user = User.objects.create_user(form.cleaned_data['scout_name'], form.cleaned_data['scout_email'], form.cleaned_data['scout_password'])
			user.save()
			return index(request)
		else:
			print form.errors
	else:
		form = ScoutRegister()
	return render(request, 'scout_app/register_scout.html', { 'form' : form})

def scout_login(request):
	if request.method == 'POST':
		form = ScoutLogin(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['user'], password=form.cleaned_data['password'])
			if user is not None:
				return index(request)
			else:
				return scout_login(request)
		else:
			print form.errors
	else:
		form = ScoutLogin()
	return render(request, 'scout_app/scout_login.html', { 'form' : form })

def scout_start(request):
	if request.method == 'POST':
        	form = TeamInfoForm(request.POST)
        	if form.is_valid():
            		form.save()
			return place_bets(request)
        	else:
        	    print form.errors
    	else:
        	form = TeamInfoForm()

	return render(request, 'scout_app/scout_start.html',{ 'form' : form})

def place_bets(request):
	if request.method == 'POST':
		form = PlaceBetForm(request.POST)
		if form.is_valid():
			form.save()
			return auto_input(request)
		else:
			print form.errors
	else:
		form = PlaceBetForm(initial={'match_number' : TeamInfoForm.cleaned_data['match_number']})
	
	return render(request, 'scout_app/place_bets.html', {'form' : form})

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
	latest_match_list = TeamData.objects.order_by('-match_number')[:6]

	if request.method == 'POST':
		form = TeamLookupForm(request.POST)
		if form.is_valid():
			return team_lookup(request, form.cleaned_data['team_number'])
		else:
			print form.errors
	else:
		 form = TeamLookupForm()

	try:
		context = {'latest_match_list' : latest_match_list, 'match_number' : latest_match_list[0].match_number, 'form' : form}
		return render(request, 'scout_app/view_data.html', context)
	except(IndexError):
                context = {'latest_match_list' : latest_match_list}
                return render(request, 'scout_app/view_data.html', context)

def team_lookup(request, team_number):
	auto_data = AutoData.objects.order_by('match_number')
	teleop_data = TeleopData.objects.order_by('match_number')
	team_auto_data = []
	team_teleop_data = []
	for team in auto_data:
		if team.team_number == int(team_number):
			team_auto_data.append(team)
	for team in teleop_data:
		if team.team_number == int(team_number):
			team_teleop_data.append(team)
	context = {'team_number' : team_number, 'team_auto_data' : team_auto_data, 'team_teleop_data' : team_teleop_data}
	return render(request, 'scout_app/team_results.html', context)

def match_lookup(request, match_number):
	context = {'match_number' : match_number}
	return render(request, 'scout_app/match_results.html', context)
