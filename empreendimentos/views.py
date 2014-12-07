# -*-coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse

from models import *


def empreendimentos(request):
    
    empreendimentos = CadastroEmpreendimento.objects.filter(ativo=True)

    VARS = {
        'empreendimentos': empreendimentos,
    }

    return render_to_response(
        'empreendimentos.html', VARS, context_instance=RequestContext(request)
    )


def restrita_empreendimentos(request):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')

    empreendimentos = CadastroEmpreendimento.objects.filter(
        ativo=True).exclude(status=4)

    VARS = {
        'empreendimentos': empreendimentos,
    }

    return render_to_response('restrita_empreendimentos.html', VARS,
        context_instance=RequestContext(request)
    )


def espelho_vendas(request, slug):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')

    empreendimento = get_object_or_404(CadastroEmpreendimento, slug=slug)
    unidades = CadastroUnidade.objects.filter(empreendimento=empreendimento)

    VARS = {
        'empreendimento': empreendimento,
        'unidades': unidades,
    }

    return render_to_response(
        'espelho_vendas.html', VARS, context_instance=RequestContext(request)
    )


def comprar_unidade(request, slug_e, slug_u):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')    
    
    # empreendimento = get_object_or_404(CadastroEmpreendimento, slug=slug)
    unidade = get_object_or_404(
        CadastroUnidade, empreendimento__slug=slug_e, slug=slug_u
    )

    try:
        unidade.status = 3
        unidade.save()
        return HttpResponseRedirect('/empreendimentos/vendido/')
    except:
        return HttpResponse('erro_venda')


def reservar_unidade(request, slug_e, slug_u):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')

    # empreendimento = get_object_or_404(CadastroEmpreendimento, slug=slug)
    unidade = get_object_or_404(
        CadastroUnidade, empreendimento__slug=slug_e, slug=slug_u
    )

    try:
        unidade.status = 2
        unidade.save()
        return HttpResponseRedirect('/empreendimentos/reservado/')
    except:
        return HttpResponse('erro_reserva')


def detalhes_empreendimento(request, slug):
    
    empreendimento = get_object_or_404(
        CadastroEmpreendimento, slug=slug, ativo=True)
    fotos = Foto.objects.filter(empreendimento=empreendimento)
    plantas = Plantas.objects.filter(empreendimento=empreendimento)

    VARS = {
        'empreendimento': empreendimento,
        'fotos': fotos,
        'plantas': plantas,
    }

    return render_to_response('detalhes_empreendimentos.html', VARS,
        context_instance=RequestContext(request)
    )


def detalhes_unidade(request, slug_e, slug_u):
    
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')

    empreendimento = get_object_or_404(
        CadastroEmpreendimento, slug=slug_e, ativo=True)
    unidade = get_object_or_404(
        CadastroUnidade, slug=slug_u, empreendimento=empreendimento
    )
    fotos = FotosUnidade.objects.filter(unidade=unidade)

    VARS = {
        'empreendimento': empreendimento,
        'unidade': unidade,
        'fotos': fotos,
    }

    return render_to_response('detalhes_unidades.html', VARS,
        context_instance=RequestContext(request)
    )    



