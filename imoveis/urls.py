# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',

	url(r'^$', 'imoveis.views.imoveis', name='imoveis'),
    url(r'^restrita-imoveis/$', 'imoveis.views.restrita_imoveis', name='restrita_imoveis'),
	url(r'^comprar/(?P<slug>[\w_-]+)/$', 'imoveis.views.comprar_imovel', name='comprar'),
	url(r'^alugar/(?P<slug>[\w_-]+)/$', 'imoveis.views.alugar_imovel', name='alugar'),
	url(r'^detalhes-imoveis/(?P<slug>[\w_-]+)/$', 'imoveis.views.detalhes_imoveis', name='detalhes_imoveis'),
	
	url(r'^reservado/$', TemplateView.as_view(template_name='reservado.html'), name="reservado"),
	url(r'^vendido/$', TemplateView.as_view(template_name='vendido.html'), name="vendido"),
)