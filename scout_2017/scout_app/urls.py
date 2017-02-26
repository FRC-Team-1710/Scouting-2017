from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^scout_start/$', views.scout_start, name='scout_start'),
    url(r'^auto_scout/$', views.auto_input, name="auto_scout"),
]
