# -*- coding: utf-8 -*-

from django.contrib import admin
from models import CadastroImoveis, FotosImoveis


class FotosImoveisInline(admin.TabularInline):
    model = FotosImoveis
    extra = 4


class CadastroImoveisAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cidade', 'estado', 'imagemAdmin', 'ativo')
    search_fields = ('titulo', 'cidade',)
    list_filter = ['ativo', 'estado', 'destaque', 'possui_suite']
    save_on_top = True
    list_per_page = 20
    prepopulated_fields = {'slug': ("titulo",)}

    inlines = [FotosImoveisInline,]


admin.site.register(CadastroImoveis, CadastroImoveisAdmin)