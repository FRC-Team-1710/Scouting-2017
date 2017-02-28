from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^scout_start/$', views.scout_start, name='scout_start'),
    url(r'^scout_auto/$', views.auto_input, name='scout_auto'),
    url(r'^scout_teleop/$', views.teleop_input, name = 'scout_teleop'),
    url(r'^view_data/$', views.view_data, name = 'view_data'),
    url(r'^team/(?P<team_number>[0-7000]+)/$', views.team_lookup, name = 'team_lookup'),
    url(r'^match/(?P<match_number>[0-200]+)/$', views.match_lookup, name = 'match_lookup'),
]
