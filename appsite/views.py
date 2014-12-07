# -*- coding: utf-8 -*-

from django import forms
from django.core.mail import send_mail
from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth import authenticate, logout, login as auth_login
from django.views.generic import TemplateView

from captcha.fields import CaptchaField
from appsite.forms import FormLogin

from empreendimentos.models import CadastroEmpreendimento
from banners.models import Banner
from imoveis.models import CadastroImoveis


class CaptchaForm(forms.Form):
    captcha = CaptchaField()


@csrf_exempt
def alteraImgCaptcha(request):

    form = CaptchaForm()
    return HttpResponse(form.as_p())


class HomeView(TemplateView):

    def get_context_data(self, **kwargs):

        banners = Banner.objects.filter(ativo=True).order_by('ordem')
        empreendimentos = CadastroEmpreendimento.objects.filter(
            ativo=True, destaque=True
        )
        imoveis = CadastroImoveis.objects.filter(ativo=True, destaque=True)

        kwargs.update({
            'banners': banners,
            'empreendimentos': empreendimentos,
            'imoveis': imoveis,
        })

        return kwargs


def form_login(request):

    form = FormLogin()

    VARS = {
        'form': form,
    }

    return render_to_response(
        'login.html', VARS, context_instance=RequestContext(request)
    )


def login(request):

    if request.POST:
        username = request.POST.get('login')
        password = request.POST.get('senha')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponse('sucesso')
                # Redirect to a success page.
            else:
                return HttpResponse('erro_usuario')
                # Return a 'disabled account' error message
        else:
            return HttpResponse('erro_login')
            # Return an 'invalid login' error message.


def area_restrita(request):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')

    return render_to_response(
        'area_restrita.html', context_instance=RequestContext(request)
    )


def sair(request):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')

    logout(request)

    return HttpResponseRedirect('/')
