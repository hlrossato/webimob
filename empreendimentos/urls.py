# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',

	url(r'^$', 'empreendimentos.views.empreendimentos', name='empreendimentos'),
    url(r'^restrita-empreendimentos/$', 'empreendimentos.views.restrita_empreendimentos', name='restrita_empreendimentos'),
	url(r'^espelho-vendas/(?P<slug>[\w_-]+)/$', 'empreendimentos.views.espelho_vendas', name='espelho_vendas'),
	url(r'^comprar-unidade/(?P<slug_e>[\w_-]+)/(?P<slug_u>[\w_-]+)/$', 'empreendimentos.views.comprar_unidade', name='comprar_unidade'),
	url(r'^reservar-unidade/(?P<slug_e>[\w_-]+)/(?P<slug_u>[\w_-]+)/$', 'empreendimentos.views.reservar_unidade', name='reservar_unidade'),
	url(r'^detalhes-empreendimento/(?P<slug>[\w_-]+)/$', 'empreendimentos.views.detalhes_empreendimento', name='detalhes_empreendimento'),
	url(r'^detalhes-unidade/(?P<slug_e>[\w_-]+)/(?P<slug_u>[\w_-]+)/$', 'empreendimentos.views.detalhes_unidade', name='detalhes_unidade'),

	url(r'^reservado/$', TemplateView.as_view(template_name='reservado_unidade.html'), name="reservado"),
	url(r'^vendido/$', TemplateView.as_view(template_name='vendido_unidade.html'), name="vendido"),	
)