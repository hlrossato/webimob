# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from models import *

from datetime import datetime, date, time


def duplicar_empreendimento(modeladmin, request, queryset):

    if not request.user.is_staff:
        raise PermissionDenied

    opts = modeladmin.model._meta

    for e in queryset:

        fotos = e.foto_set.all()
        plantas = e.plantas_set.all()

        new = e

        # deletando id para inserir novo produto
        new.id = None
        new.slug += "-copy"

        new.save()      

        for f in fotos:
            f.id = None
            f.empreendimento = new
            f.save()

        for p in plantas:
            p.id = None
            p.empreendimento = new
            p.save()

    return HttpResponse('Empreendimentos Duplicados com Sucesso!') 

duplicar_empreendimento.short_description = "Duplicar Empreendimentos"


def duplicar_unidades(modeladmin, request, queryset):
    
    if not request.user.is_staff:
        raise PermissionDenied

    opts = modeladmin.model._meta

    for u in queryset:

        fotos = u.fotosunidade_set.all()

        new = u

        new.id = None
        new.slug += "-copy"

        new.save()

        for f in fotos:
            f.id = None
            f.unidade = new
            f.save()

    return HttpResponse('Unidades Duplicadas com Sucesso!')

duplicar_unidades.short_description = "Duplicar Unidades"


def liberar_unidades(modeladmin, request, queryset):
    
    if not request.user.is_staff:
        raise PermissionDenied

    opts = modeladmin.model._meta

    for u in queryset:

        u.status = 1
        u.save()

    return HttpResponse('Unidades Liberadas com Sucesso!')

liberar_unidades.short_description = "Liberar Unidades"        


