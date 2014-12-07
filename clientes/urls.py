# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
	
    url(r'^pre-cadastro-cliente/$', 'clientes.views.pre_cadastro_clientes', name="pre_cadastro_clientes"),
    url(r'^pre-cadastro-clientes/send/$', 'clientes.views.pre_cadastro_send', name="pre_cadastro_send"),
    url(r'^cadastro-cliente/$', 'clientes.views.cadastro_clientes', name="cadastro_clientes"),
    url(r'^cadastro-cliente/send/$', 'clientes.views.cadastro_clientes_send', name="cadastro_clientes_send"),
)