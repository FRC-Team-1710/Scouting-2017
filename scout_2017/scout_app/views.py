from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from scout_app.models import TeamData, AutoData, TeleopData, BetHandler, Scout, Bet, OtherData, Comments, Teams
from scout_app.forms import forms, TeamInfoForm, AutoInfoForm, TeleopInfoForm, TeamLookupForm, PlaceBetForm, ScoutRegister, ScoutLogin, TeamFilterForm, CommentForm
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import matplotlib.pyplot as plt
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/scout/')
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
				return HttpResponse("login failed")
		else:
			print form.errors
	else:
		form = ScoutLogin()
	return render(request, 'scout_app/scout_login.html', { 'form' : form })

@login_required
def scout_start(request):
	errors = None
	scouts = Scout.objects.order_by('user')
	matches = TeamData.objects.order_by('-match_number')
	teams = Teams.objects.order_by('team_number')
	match_played = False
	team_exists = False
	match_count = 0

	if request.method == 'POST':
        	form = TeamInfoForm(request.POST)
        	if form.is_valid():
			for match in matches:
				if str(match.match_number) == str(form.cleaned_data['match_number']):
					match_count += 1
					print "sweet yeet " + str(match_count) 
					if match_count >= 6:
						errors = "Match Already Played"
						match_played = True
			for team in teams:
				if str(form.cleaned_data['team_number']) == str(team.team_number):
					team_exists = True
			if match_played == False and team_exists == True:
				new_team = TeamData(match_number = form.cleaned_data['match_number'], team_number = form.cleaned_data['team_number'], alliance_color = form.cleaned_data['alliance_color'], current_scout=request.user.username)
				new_team.save()
				return HttpResponseRedirect('/scout/place_bets/')
			else:
				errors = "That team is not competing here"
        	else:
        	    print form.errors
    	else:
        	form = TeamInfoForm()

	return render(request, 'scout_app/scout_start.html',{ 'form' : form, 'errors' : errors})

@login_required
def place_bets(request):
	if request.method == 'POST':
		form = PlaceBetForm(request.POST)
        	form.fields['match_number'].widget = forms.HiddenInput()
		matches = TeamData.objects.order_by('match_number')
       		#finds match number
		team_num = 0
		match_num = 0
        	for match in matches:
                	if str(match.current_scout) == str(request.user.username):
                        	match_num = match.match_number
				team_num = match.team_number

		if form.is_valid():
			current_scout = None
			scouts = Scout.objects.order_by('user')
			for scout in scouts:
				if scout.user == request.user.username:
					current_scout = scout

			if int(form.cleaned_data['alliance_money']) > 0 and current_scout.scout_sheckles >= int(form.cleaned_data['alliance_money']):
				new_bet = Bet(user = str(request.user.username), match_number=match_num, alliance_bet_on=form.cleaned_data['bet_alliance'], money_bet=form.cleaned_data['alliance_money'])
	                        new_bet.save()
				new_balance = current_scout.scout_sheckles - int(form.cleaned_data['alliance_money'])
        	                current_scout.scout_sheckles = new_balance
				current_scout.save()
	                        form.save()
				return auto_input(request)
			elif int(form.cleaned_data['alliance_money']) <= 0:
				return auto_input(request)
			else:
				HttpResponseRedirect('/scout/place_bets/')
		else:
			print form.errors
	else:
		form = PlaceBetForm()
		form.fields['match_number'].widget = forms.HiddenInput()
	return render(request, 'scout_app/place_bets.html', {'form' : form})
@login_required
def auto_input(request):
	matches = TeamData.objects.order_by('match_number')
	scouts = Scout.objects.order_by('user')
        team_num = 0
        match_num = 0
        for match in matches:
        	if str(match.current_scout) == str(request.user.username):
        		match_num = match.match_number
        		team_num = match.team_number

	if request.method == 'POST':
		form = AutoInfoForm(request.POST)
		if form.is_valid():
			form.save()
			return teleop_input(request)
		else:
			print form.errors
	else:
		print "meme"

	print "hey " + str(match_num)
	form = AutoInfoForm(initial={'team_number' : team_num,
				     'match_number' : match_num, "auto_fuel_accuracy" : 0})
#        form.fields['match_number'].widget = forms.HiddenInput()
#        form.fields['team_number'].widget = forms.HiddenInput()

	return render(request, 'scout_app/scout_auto.html', {'form' : form, 'team_number' : team_num, 'match_number' : match_num})
@login_required
def teleop_input(request):
        matches = TeamData.objects.order_by('match_number')
	scouts = Scout.objects.order_by('user')
        team_num = 0
        match_num = 0
        for match in matches:
        	if str(match.current_scout) == str(request.user.username):
        		match_num = match.match_number
        		team_num = match.team_number


	if request.method == 'POST':
                form = TeleopInfoForm(request.POST)
                if form.is_valid():
                        form.save()
			#give scout 50 scheckles and add a match to their matches scouted count
                        for scout in scouts:
				if str(scout.user) == str(request.user.username):
					new_balance = scout.scout_sheckles + 50
					scout.scout_sheckles = new_balance
					updated_matches_scouted = scout.matches_scouted + 1
					scout.matches_scouted = updated_matches_scouted
					scout.save()

			return HttpResponseRedirect('/scout/thanks')
                else:
                        print form.errors
        else:
		print "killme"

        form = TeleopInfoForm(initial={'team_number' : team_num,
                                        'match_number' : match_num, "teleop_fuel_accuracy" : 0})

#        form.fields['match_number'].widget = forms.HiddenInput()
#        form.fields['team_number'].widget = forms.HiddenInput()

        return render(request, 'scout_app/scout_teleop.html', {'form' : form, 'team_number' : team_num, 'match_number' : match_num})
def thanks(request):
	scouts = Scout.objects.order_by('user')
	matches = TeamData.objects.order_by('match_number')
	matches_scouted = 0
	return_home = "go back home"
	motivation = "Check the status of your bet"
	match_num = 0
	team_num = 0
        for match in matches:
                if str(match.current_scout) == str(request.user.username):
                        match_num = match.match_number
                        team_num = match.team_number

	for scout in scouts:
		if str(scout.user) == str(request.user):
			matches_scouted = int(scout.matches_scouted)
	return render(request, 'scout_app/thanks.html', {"matches_scouted" : matches_scouted, "motivation" : motivation, "return_home" : return_home, 'match_number' : match_num})
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
		context = {'latest_match_list' : latest_match_list, 'match_number' : latest_match_list[0].match_number, 'form' : form, "id" : 1}
		return render(request, 'scout_app/view_data.html', context)
	except(IndexError):
                context = {'latest_match_list' : latest_match_list, "id" : 1}
                return render(request, 'scout_app/view_data.html', context)

def filter_data(request):
	matches  = TeleopData.objects.order_by('match_number')
	context = {}
	if request.method == 'POST':
		form = TeamFilterForm(request.POST)
		if form.is_valid():
			print form.cleaned_data['filter_type']
 			if form.cleaned_data['filter_type'] == u"most gears in teleop":
				matches = TeleopData.objects.order_by('-gears_placed')
				context = {'gears' : matches}
				return render(request, 'scout_app/filter.html', context)
			elif form.cleaned_data['filter_type'] == u"perfect climbers":
				teams = []
				perfect_climbing = []
				teams_ = TeamData.objects.order_by('team_number')
				team_num = 0
				previous_team = 0
				for team in teams_:
					team_num = team.team_number
					if team_num != previous_team:
						#calculate climbing percentage
						count = 0
						success = 0
						for match in matches:
							if str(match.team_number) == str(team_num):
								if match.climber_success == u"climbed successfully":
									success += 1
								count += 1
						#print (float(success)/float(count)) * 100
						print count
						if count != 0 and (float(success)/float(count)) * 100 >= 100:
							perfect_climbing.append(str(team_num))
							print "hey"
					previous_team = team_num
				print perfect_climbing
				context = {'perfect_teams' : perfect_climbing}
				return render(request, 'scout_app/filter.html', context)
			elif form.cleaned_data['filter_type'] == u"teams ranked by climbs":
                                teams = []
				climb_data_climbs = []
				climb_data_team = []
				climb_data = []
                                teams_ = TeamData.objects.order_by('team_number')
                                team_num = 0
                                previous_team = 0
                                for team in teams_:
                                        team_num = team.team_number
                                        if team_num != previous_team:
                                                #calculate climbing percentage
                                                count = 0
                                                success = 0
                                                for match in matches:
                                                        if str(match.team_number) == str(team_num):
                                                                if match.climber_success == u"climbed successfully":
                                                                        success += 1
								count += 1
						if count != 0:
							climb_data.append([team_num, (float(success)/float(count)) * 100])
                                        previous_team = team_num
                                context = {'climb_data': sorted(climb_data, key = lambda x : x[1], reverse=True)}
                                return render(request, 'scout_app/filter.html', context)
		else:
			print form.errors
	else:
		form = TeamFilterForm()
		context = {"id" : 2, 'form' : form}
	return render(request, 'scout_app/view_data.html', context)

def team_lookup(request, team_number):
	auto_data = AutoData.objects.order_by('match_number')
	teleop_data = TeleopData.objects.order_by('match_number')
	comments_all = Comments.objects.order_by('scout')
	comments_for_team = []
	team_auto_data = []
	team_teleop_data = []
	teleop_gears_placed =[]
	xAxis = []
	gear_sum = 0
	count = 0
	#raw data in tables
	for team in auto_data:
		if team.team_number == int(team_number):
			team_auto_data.append(team)
	for team in teleop_data:
		if team.team_number == int(team_number):
			team_teleop_data.append(team)
			teleop_gears_placed.append(team.gears_placed)
	for gear in teleop_gears_placed:
		gear_sum += gear
		count += 1
	gear_average = float(gear_sum)/float(count)

	count = 0
	climb_count = 0

	for climb in teleop_data:
		if str(climb.team_number) == str(team_number):
			if climb.climber_success == u"climbed successfully":
				climb_count += 1
			count += 1

	climb_p = (float(climb_count)/float(count)) * 100

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form = Comments(scout=request.user.username, comment=form.cleaned_data['comment'], team_number = team_number)
			form.save()
		else:
			print form.errors
	else:
		form = CommentForm()

	for comment in comments_all:
		if str(comment.team_number) == str(team_number):
			comments_for_team.append(comment)

	new_other = OtherData(team_number=team_number, climb_percentage = climb_p, gear_average = gear_average)
	context = {'team_number' : team_number, 'team_auto_data' : team_auto_data, 'team_teleop_data' : team_teleop_data, 'gear_average' : gear_average, 'climber_success': climb_p, 'form' : form, 'comments' : comments_for_team}
	return render(request, 'scout_app/team_results.html', context)

def export_raw(request):
	import csv
	teleop_data = TeleopData.objects.order_by('match_number')
	context = None

	response = HttpResponse(content_type='text/csv')

        response['Content-Disposition'] = 'attachment; filename="kc_raw.csv"'

	with open('kc_raw.csv', 'wb') as csvfile:
		raw_data = csv.writer(response)
		raw_data.writerow(['Match Number', 'Team Number', 'Gears Placed', 'Fuel Scored', 'Climber Success'])
		for match in teleop_data:
			if int(match.match_number) > 6:
				match_row = [str(match.match_number), str(match.team_number), str(match.gears_placed), str(match.teleop_fuel_accuracy), str(match.climber_success)]
				raw_data.writerow(match_row)

	return response

def match_lookup(request, match_number):
	#scrapes north star schedule for match schedule
	scope = ['https://spreadsheets.google.com/feeds']
	row_num = 0
	credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/herm/Scouting-1df27c55e93e.json', scope)

	gc = gspread.authorize(credentials)

	wks = gc.open('North Star Match Schedule').sheet1

	matches = wks.col_values(1)
	print matches
	for match in matches:
		row_num += 1
		if str(match) == 'Quals ' + str(match_number):
			teams_in_match = wks.row_values(row_num)

	context = {'match_number' : match_number, 'blue_teams' : teams_in_match[1:6], 'red_teams' : teams_in_match[7:12]}
	return render(request, 'scout_app/match_results.html', context)

def logout(request):
	django_logout(request)
	return HttpResponseRedirect('/scout/')
@login_required
def my_bets(request):
	bets = Bet.objects.order_by('user')
	current_scout_bets = []
	context = {}
	for bet in bets:
		if str(bet.user) == str(request.user.username) and bet.claimed == False:
			print " yoyoyoyoyoyoy " + str(bet)
			current_scout_bets.append(bet)
			context = {'bets' : current_scout_bets} 
		else:
			print "BET ALREADY CLAIMED"
			context = {}

	return render(request, 'scout_app/my_bets.html', context)
@login_required
def view_bet(request, match_number):
	bets = Bet.objects.order_by('match_number')
	matches = TeleopData.objects.order_by('match_number')
	scouts = Scout.objects.order_by('user')
	current_bet = None
	blue_win_count = 0
	red_win_count = 0
	current_scout = None
	scout_choice = ""
	money_in_pot = 0
	winning_alliance = None
	bet_count = 0
	red_bet_count = 0
	blue_bet_count = 0
	percent_of_pot = 0.0
	context = {}
	blue_money = 0
	red_money = 0
	percent_return = 0.0
	winnings = 0
	#calculate the money in the pot for that match
	for bet in bets:
		if str(bet.match_number) == match_number:
			money_in_pot += bet.money_bet
			bet_count += 1
			print "money bet" + str(money_in_pot)
			#finds the amount of people who bet on each alliance
			if str(bet.alliance_bet_on) == "Blue Alliance":
				blue_bet_count += 1
			elif str(bet.alliance_bet_on) == "Red Alliance":
				red_bet_count += 1
	#finds current Bet instance
	for bet in bets:
		if str(bet.match_number) == match_number:
			if str(bet.user) == str(request.user.username):
				current_bet = bet

	#finds the alliance the scout bet on
	for scout in scouts:
		if str(scout.user) == str(request.user.username):
			current_scout = scout
			for bet in bets:
				if str(bet.user) == str(current_scout.user) and str(bet.match_number) == str(match_number):
					scout_choice = bet.alliance_bet_on

	#calculates money placed on each alliance
	for bet in bets:
		if str(bet.alliance_bet_on) == "Blue Alliance":
			blue_money += bet.money_bet
		elif str(bet.alliance_bet_on) == "Red Alliance":
			red_money += bet.money_bet
	#calculates return percent
	for scout in scouts:
                if str(scout.user) == str(request.user.username):
                        current_scout = scout
                        for bet in bets:
                                if str(bet.user) == str(current_scout.user) and str(bet.match_number) == str(match_number):
                                        if str(bet.alliance_bet_on) == "Blue Alliance":
						percent_return = float(bet.money_bet)/float(blue_money)
                				print "heyeyey" + str(blue_money)
					elif str(bet.alliance_bet_on) == "Red Alliance":
						percent_return = float(bet.money_bet)/float(red_money)
						print "heyTYTT"
	#organizes teams in the match
	blue_odds = 0
	red_odds = 0
	blue_teams = []
	red_teams = []
	for match in matches:
		if match.match_number == match_number:
			if str(match.alliance_color) == "Blue Alliance":
				blue_teams.append(int(match.team_number))
			else:
				red_teams.append(int(match.team_number))
	#finds the alliance most likely to win
	blue_climbs = 0
	red_climbs = 0
	for team in blue_teams:
		for match in matches:
			if str(match.climber_success) == "climbed successfully" and str(match.alliance_color) == "Blue Alliance": 
				blue_climbs += 1

        for team in red_teams:
                for match in matches:
                        if str(match.climber_success) == "climbed successfully" and str(match.alliance_color) == "Red Alliance": 
                                red_climbs += 1

	if blue_climbs > red_climbs:
		print "ugh"

	#finds the alliance that won
	for match in matches:
		if str(match.match_number) == str(match_number):
			#checks all data from the match to weed out cheaters
			if str(match.winning_alliance) == "Blue Alliance":
				blue_win_count += 1
			else:
				red_win_count += 1

	if blue_win_count > red_win_count:
		winning_alliance = "Blue Alliance"
	elif red_win_count > blue_win_count:
		winning_alliance = "Red Alliance"
	else:
		winning_alliance = "tie"
		#move pot money into the pot of the next match
	if str(scout_choice) == str(winning_alliance):
		print "odds multiplier" + str(percent_return)
		winnings = money_in_pot * percent_return

		if current_bet.claimed == False:
			current_bet.claimed = True
			current_bet.save()
			print current_bet.claimed
			new_balance = current_scout.scout_sheckles + winnings
			current_scout.scout_sheckles = new_balance
			current_scout.save()
			print "sheckles claimed"
		else:
			print "sheckles already claimed"

		context = {'pot_money' : money_in_pot, 'alliance_bet_on' : str(scout_choice), 'winning_alliance' : str(winning_alliance), 'winnings' : winnings}
	else:
		context = {'pot_money' : money_in_pot, 'alliance_bet_on' : str(scout_choice), 'winnning_alliance' : str(winning_alliance)}

	return render(request, 'scout_app/bet_viewer.html', context)
