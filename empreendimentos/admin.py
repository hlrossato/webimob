# -*- coding: utf-8 -*-


from django.contrib import admin
from models import CadastroEmpreendimento, Foto, CadastroUnidade, FotosUnidade, Plantas
from actions import duplicar_empreendimento, duplicar_unidades, liberar_unidades


class FotoEmpreendimentoInline(admin.TabularInline):
    model = Foto
    extra = 4


class PlantasInline(admin.TabularInline):
    model = Plantas
    extra = 4


class FotosUnidadeInline(admin.TabularInline):
    model = FotosUnidade
    extra = 4


class CadastroEmpreendimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'estado', 'status', 'imagemAdmin', 'ativo')
    search_fields = ('nome', 'descricao', 'cidade', 'estado')
    list_filter = ['ativo', 'status', 'estado', 'destaque',]
    save_on_top = True
    list_per_page = 20
    prepopulated_fields = {'slug': ("nome",)}
    actions = [duplicar_empreendimento]

    inlines = [FotoEmpreendimentoInline, PlantasInline]


class CadastroUnidadeAdmin(admin.ModelAdmin):
    list_display = (
        'empreendimento', 'titulo', 'andar', 'qtde_quartos', 'qtde_banheiros',
        'possui_suite', 'status', 'imagemAdmin'
    )
    search_fields = ('titulo', 'andar')
    list_filter = ['qtde_quartos', 'qtde_banheiros', 'possui_suite']
    save_on_top = True
    list_per_page = 20
    prepopulated_fields = {'slug': ("titulo",)}
    actions = [duplicar_unidades, liberar_unidades]

    inlines = [FotosUnidadeInline,]


admin.site.register(CadastroUnidade, CadastroUnidadeAdmin)
admin.site.register(CadastroEmpreendimento, CadastroEmpreendimentoAdmin)