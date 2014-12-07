# -*- coding: utf-8 -*-

from django.db import models
from localflavor.br.br_states import STATE_CHOICES


class Email(models.Model):

    class Meta:
        verbose_name = u'Emails para recebimento'
        verbose_name_plural = u'Emails para recebimento'

    nome = models.CharField(verbose_name=u'Nome', max_length=255)
    email = models.EmailField(
    	verbose_name=u'Email', max_length=255,
    	help_text=u"""Lembre-se, o email aqui inserido deve estar vinculado a 
    	um assunto para receber as mensagens."""
    )

    def __unicode__(self):
        return self.nome + ' - ' + self.email


class Assunto(models.Model):
    nome = models.CharField(verbose_name=u'Nome', max_length=255)
    email_assunto = models.ManyToManyField(
    	Email, help_text=u'Emails para receber contatos deste assunto'
    )

    class Meta:
        ordering = ('nome',)
        verbose_name = u'Assunto'
        verbose_name_plural = u'Assuntos'

    def __unicode__(self):
        return self.nome


class Contato(models.Model):

    class Meta:
        ordering = ('nome',)
        verbose_name = u'Contato'
        verbose_name_plural = u'Contatos'

    assunto = models.ForeignKey(Assunto, verbose_name="Assunto")
    nome = models.CharField(verbose_name=u"Nome", max_length=255)
    email = models.EmailField(verbose_name="Email")
    telefone = models.CharField(
        verbose_name="Telefone", max_length=20, blank=True, null=True
    )
    mensagem = models.TextField(verbose_name="Mensagem")
    data = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.nome