# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Email, Assunto, Contato
from webimob.action import export_as_csv


class EmailAdmin(admin.ModelAdmin):

    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    # list_filter = ['campo2']
    save_on_top = True
    list_per_page = 20


class AssuntoAdmin(admin.ModelAdmin):

    list_display = ('nome',)
    search_fields = ('nome',)
    # list_filter = ['campo2']
    save_on_top = True
    list_per_page = 20

    filter_horizontal = ['email_assunto', ]


class ContatoAdmin(admin.ModelAdmin):

    list_display = ('assunto', 'nome', 'email', 'data')
    search_fields = ('assunto', 'nome', 'email',)
    list_filter = ['assunto', 'data', ]
    save_on_top = True
    list_per_page = 20
    actions = [export_as_csv]


admin.site.register(Assunto, AssuntoAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Email, EmailAdmin)