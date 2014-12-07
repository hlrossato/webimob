# -*-coding: utf-8 -*-

from django.core.mail import send_mail
from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
import datetime
import time
from decimal import Decimal

from models import PreCadastroCliente, CadastroCliente, EmailsRecebimento
from forms import FormPreCadastroCliente, FormCadastroCliente


def pre_cadastro_clientes(request):

    form = FormPreCadastroCliente()

    VARS = {
        'form': form,
    }

    return render_to_response(
        'pre_cadastro_clientes.html', VARS, 
        context_instance=RequestContext(request)
    )


def pre_cadastro_send(request, template='email/precadastro.txt'):

    if request.POST:

        form = FormPreCadastroCliente(request.POST)

        if form.is_valid():

            form.save()
            cliente = PreCadastroCliente.objects.filter(
                nome=form.cleaned_data['nome']
            )

            if 'continuar' in request.POST and cliente:
                return HttpResponse(cliente[0].id)
            else:
                t = loader.get_template(template)
                f = Context(form.dados())

                emails = EmailsRecebimento.objects.all()
                destinatarios = []

                for e in emails:
                    destinatarios.append(e.email)            

                send_mail(
                    u'WebImob Pré-Cadastro de Clientes', t.render(f),
                    u'WebImob Pré-Cadastro de Clientes{0}'.format(settings.EMAIL_HOST_USER),
                    destinatarios, fail_silently=False
                )

            return HttpResponse('sucesso')

        return HttpResponse(form.errors)


def cadastro_clientes(request):

    cliente = None

    if request.GET.get('c_id'):
        cliente = PreCadastroCliente.objects.get(
            id=int(request.GET.get('c_id'))
        )
        form = FormCadastroCliente(instance=cliente)
    else:
        form = FormCadastroCliente()

    VARS = {
        'form': form,
        'cliente': cliente
    }

    return render_to_response(
        'cadastro_clientes.html', VARS, context_instance=RequestContext(request)
    )


def cadastro_clientes_send(request, template='email/cadastroclientes.txt'):

    if request.POST:

        form = FormCadastroCliente(request.POST)           

        if form.is_valid():

            cli = CadastroCliente.objects.filter(cpf=request.POST.get('cpf'))

            if cli:
                return HttpResponse('cpf_existe')

            # convertendo data para o padrão correto aaaa-mm-dd
            aux = request.POST.get('data_nascimento').split('/')
            data_nascimento = datetime.date(
                int(aux[2]), int(aux[1]), int(aux[0])
            )

            # verificando se existe o campo de data de nascimento do conjuge para converter
            if request.POST.get('data_nascimento_conjuge'):
                aux1 = request.POST.get('data_nascimento_conjuge').split('/')
                data_nascimento_conjuge = datetime.date(
                    int(aux1[2]), int(aux1[1]), int(aux1[0])
                )
            else:
                data_nascimento_conjuge = None

            if request.POST.get('profissao_conjuge'):
                profissao_conjuge = request.POST.get('profissao_conjuge')
            else:
                profissao_conjuge = None

            if request.POST.get('filhos'):
                filhos = request.POST.get('filhos')
            else:
                filhos = None

            if request.POST.get('qtde_filhos'):
                qtde_filhos = request.POST.get('qtde_filhos')
            else:
                qtde_filhos = None

            if request.POST.get('c_id'):
                cliente = PreCadastroCliente.objects.get(
                    id=int(request.POST.get('c_id'))
                )

                c = CadastroCliente(
                    pre_cadastro = cliente,
                    nome = request.POST.get('nome'),
                    email = request.POST.get('email'),
                    telefone = request.POST.get('telefone'),
                    celular = request.POST.get('celular'),
                    data_nascimento = data_nascimento,
                    rg = request.POST.get('rg'),
                    cpf = request.POST.get('cpf'),
                    endereco = request.POST.get('endereco'),
                    cidade = request.POST.get('cidade'),
                    estado = request.POST.get('estado'),
                    estado_civil = request.POST.get('estado_civil'),
                    profissao = request.POST.get('profissao'),
                    nome_conjuge = request.POST.get('nome_conjuge'),
                    telefone_conjuge = request.POST.get('telefone_conjuge'),
                    celular_conjuge = request.POST.get('celular_conjuge'),
                    data_nascimento_conjuge = data_nascimento_conjuge,
                    rg_conjuge = request.POST.get('rg_conjuge'),
                    cpf_conjuge = request.POST.get('cpf_conjuge'),
                    endereco_conjuge = request.POST.get('endereco_conjuge'),
                    profissao_conjuge = profissao_conjuge,
                    faixa_salarial = request.POST.get('faixa_salarial'),
                    filhos = filhos,
                    qtde_filhos = qtde_filhos
                )

                c.save()
            else:
                form.save()

            t = loader.get_template(template)
            f = Context(form.dados())

            emails = EmailsRecebimento.objects.all()
            destinatarios = []

            for e in emails:
                destinatarios.append(e.email)            

            send_mail(
                u'WebImob Cadastro de Clientes', t.render(f),
                'WebImob Cadastro de Clientes{0}'.format(settings.EMAIL_HOST_USER),
                destinatarios, fail_silently=False
            )

            return HttpResponse('sucesso')

        return HttpResponse(form.errors)
