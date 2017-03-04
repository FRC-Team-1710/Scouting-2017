from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from scout_app.models import TeamData, AutoData, TeleopData, BetHandler, Scout, Bet
from scout_app.forms import forms, TeamInfoForm, AutoInfoForm, TeleopInfoForm, TeamLookupForm, PlaceBetForm, ScoutRegister, ScoutLogin
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

import variables_n_shit as var

def index(request):
	context = {} 
	print type(request.user.username)
	if request.user.username:
		scouts = Scout.objects.order_by('scout_sheckles')
		current_scout = None
		for scout in scouts:
			if str(scout.user) == str(request.user.username):
				current_scout = scout
		print request.user.username
		context = {'user' : request.user, 'scout' : current_scout}
	else:
		context = {'user' : 42}

	return render(request, 'scout_app/index.html', context)

def scout_register(request):
	if request.method == 'POST':
		form = ScoutRegister(request.POST)
		if form.is_valid():
			user = User.objects.create_user(form.cleaned_data['scout_name'], form.cleaned_data['scout_email'], form.cleaned_data['scout_password'])
			user.save()
			new_scout = Scout(user = form.cleaned_data['scout_name'], scout_sheckles = 100)
			new_scout.save()
			user = authenticate(username=form.cleaned_data['scout_name'], password=form.cleaned_data['scout_password'])
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
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/scout/')
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
			var.current_match = form.cleaned_data['match_number']
			var.current_team = form.cleaned_data['team_number']
			return place_bets(request)
        	else:
        	    print form.errors
    	else:
        	form = TeamInfoForm()

	return render(request, 'scout_app/scout_start.html',{ 'form' : form})

def place_bets(request):
	if request.method == 'POST':
		form = PlaceBetForm(request.POST)
        	form.fields['match_number'].widget = forms.HiddenInput()
		if form.is_valid():
			new_bet = Bet(user = str(request.user.username), match_number=var.current_match, alliance_bet_on=form.cleaned_data['bet_alliance'])
			form.save()
			new_bet.save()
			return auto_input(request)
		else:
			print form.errors
	else:
		form = PlaceBetForm()
		form.fields['match_number'].widget = forms.HiddenInput()
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
		print "meme"

	form = AutoInfoForm(initial={'team_number' : var.current_team,
				     'match_number' : var.current_match})

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
                form = TeleopInfoForm(initial={'team_number' : var.current_team, 
                                             'match_number' : var.current_match})

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

def logout(request):
	django_logout(request)
	return HttpResponseRedirect('/scout/')

def my_bets(request):
	bets = Bet.objects.order_by('user')
	current_scout_bets = None
	context = {}
	for bet in bets:
		if bet.user == request.user.username:
			current_scout_bets.append(bet)
			context 
	return render(request, 'scout_app/my_bets.html', context)
