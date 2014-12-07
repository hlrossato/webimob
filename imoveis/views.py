# -*-coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse

from models import *


def imoveis(request):
    
    imoveis = CadastroImoveis.objects.filter(ativo=True, status=1)

    VARS = {
        'imoveis': imoveis,
    }

    return render_to_response(
        'imoveis.html', VARS, context_instance=RequestContext(request)
    )


def restrita_imoveis(request):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')

    imoveis = CadastroImoveis.objects.filter(
        ativo=True, status=1)

    VARS = {
        'imoveis': imoveis,
    }

    return render_to_response('restrita_imoveis.html', VARS,
        context_instance=RequestContext(request)
    )


def detalhes_imoveis(request, slug):
    
    imovel = get_object_or_404(CadastroImoveis, slug=slug, ativo=True)
    fotos = FotosImoveis.objects.filter(imovel=imovel)

    VARS = {
        'imovel': imovel,
        'fotos': fotos,
    }

    return render_to_response('detalhes_imoveis.html', VARS,
        context_instance=RequestContext(request)
    )


def comprar_imovel(request, slug):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')    
    
    imovel = get_object_or_404(CadastroImoveis, slug=slug)

    try:
        imovel.status = 3
        imovel.save()
        return HttpResponseRedirect('/imoveis/vendido/')
    except:
        return HttpResponse('erro_venda')


def alugar_imovel(request, slug):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')

    imovel = get_object_or_404(CadastroImoveis, slug=slug)

    try:
        imovel.status = 2
        imovel.save()
        return HttpResponseRedirect('/imoveis/reservado/')
    except:
        return HttpResponseRedirect('erro_reserva')
