# -*- coding: utf-8 -*-
import sys

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.views.generic import TemplateView
from appsite import views

from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # admin
    url(r'^admin/', include(admin.site.urls)),

    # appsite
    url(r'^', include('appsite.urls', namespace='appsite')),
    
    # contato
    url(r'^contato/', include('contato.urls', namespace='contato')),    
    
    # clientes
    url(r'^clientes/', include('clientes.urls', namespace='clientes')),

    #corretores
    url(r'^corretores/', include('corretores.urls', namespace='corretores')),

    # imoveis
    url(r'^imoveis/', include('imoveis.urls', namespace='imoveis')),    

    # empreendimentos
    url(r'^empreendimentos/', include('empreendimentos.urls', namespace='empreendimentos')),    

    # captcha
    url(r'^captcha/', include('captcha.urls')),
)

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
    (r'^alteraImgCaptcha/$', 'appsite.views.alteraImgCaptcha'),
)

urlpatterns += staticfiles_urlpatterns()

if len(sys.argv) >= 2 and sys.argv[1] in ('runserver', 'runserver_plus',):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)