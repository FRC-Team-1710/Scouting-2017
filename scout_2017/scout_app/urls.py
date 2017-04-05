from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^scout_start/$', views.scout_start, name='scout_start'),
    url(r'^scout_auto/$', views.auto_input, name='scout_auto'),
    url(r'^scout_teleop/$', views.teleop_input, name = 'scout_teleop'),
    url(r'^place_bets/$', views.place_bets, name = 'place_bets'),
    url(r'^scout_login/$', views.scout_login, name= 'scout_login'),
    url(r'^register_scout/$', views.scout_register, name = 'register'),
    url(r'^view_data/$', views.view_data, name = 'view_data'),
    url(r'^view_match/$', views.match_search, name = 'match_search'),
    url(r'^team/(?P<team_number>[0-9999]+)/$', views.team_lookup, name = 'team_lookup'),
    url(r'^match/(?P<match_number>[0-999]+)/$', views.match_lookup, name = 'match_lookup'),
    url(r'^logout/$', views.logout, name = 'logout'),
    url(r'^bets/$', views.my_bets, name = 'bets'),
    url(r'^bets/(?P<match_number>[0-9999]+)/$', views.view_bet, name = 'view_bet'),
    url(r'^thanks/$', views.thanks, name="thanks"),
    url(r'^filter_data/$', views.filter_data, name='filter_data'),
    url(r'^thanks_export/$', views.export_raw, name='export_raw'),
]
