# -*- coding: utf-8 -*-

from django.contrib import admin
from models import CadastroCorretor


class CadastroCorretorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    search_fields = ('nome',)
    list_filter = ['ativo', ]
    save_on_top = True
    list_per_page = 20


admin.site.register(CadastroCorretor, CadastroCorretorAdmin)