# -*- coding: utf-8 -*-

from django.contrib import admin
from models import PreCadastroCliente, CadastroCliente, EmailsRecebimento
from webimob.action import export_as_csv


class PreCadastroClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'celular', 'data_cadastro')
    search_fields = ('nome', 'email')
    list_filter = ['data_cadastro', ]
    save_on_top = True
    list_per_page = 20
    actions = [export_as_csv]


class CadastroClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'email', 'telefone', 'celular', 'cidade', 'estado', 
        'estado_civil', 'data_cadastro'
    )
    search_fields = (
        'nome', 'email', 'telefone', 'celular', 'cidade', 'estado', 'estado_civil'
    )
    list_filter = ['estado', 'estado_civil']
    save_on_top = True
    list_per_page = 20
    actions = [export_as_csv]


class EmailsRecebimentoAdmin(admin.ModelAdmin):
    list_display = ('email', )
    search_fields = ('email', )
    save_on_top = True
    list_per_page = 20


admin.site.register(EmailsRecebimento, EmailsRecebimentoAdmin)
admin.site.register(CadastroCliente, CadastroClienteAdmin)
admin.site.register(PreCadastroCliente, PreCadastroClienteAdmin)
