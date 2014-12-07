# -*- coding: utf-8 -*-

from django.core.mail import send_mail
from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings

from forms import FormContato
from models import Assunto, Email, Contato


def contato(request):

    form = FormContato()

    VARS = {
        'form': form,
    }

    return render_to_response(
        'contato.html', VARS, context_instance=RequestContext(request)
    )


def contato_send(request, template='email/contato.txt'):

    if request.POST:
        form = FormContato(request.POST)

        if form.is_valid():
            form.save()

            t = loader.get_template(template)
            f = Context(form.dados())

            destinatarios = []

            id_assunto = request.POST.get('assunto')
            assunto = Assunto.objects.filter(id=id_assunto)

            if assunto:
                assunto = assunto[0]
            emails = Email.objects.filter(assunto=assunto)

            for e in emails:
                destinatarios.append(e.email)            

            send_mail(
                u'WebImob Contato', t.render(f),
                'WebImob Contato{0}'.format(settings.EMAIL_HOST_USER),
                destinatarios, fail_silently=False
            )

            return HttpResponse('sucesso')

        return HttpResponse(form.errors)
