# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from views import contato, contato_send

urlpatterns = patterns('',
	# contato
    url(r'^$', 'contato.views.contato', name='contato'),
    url(r'^send/$', 'contato.views.contato_send', name='contato_send'),
)