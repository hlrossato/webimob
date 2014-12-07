# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from appsite.views import HomeView

urlpatterns = patterns('',
	
	# home
    url(r'^$', HomeView.as_view(template_name='home.html'), name='home'),

    # login
    url(r'^login/$', 'appsite.views.form_login', name='login'),
    url(r'^logado/$', 'appsite.views.login', name='logado'),
    url(r'^area-restrita/$', 'appsite.views.area_restrita', name='area_restrita'),
    url(r'^logout/$', 'appsite.views.sair', name='logout'),
)