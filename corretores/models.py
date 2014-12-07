# -*- coding: utf-8 -*-

from django.db import models



class CadastroCorretor(models.Model):

    class Meta:
        ordering = ('nome', )
        verbose_name = 'Cadastro de Corretor'
        verbose_name_plural = 'Cadastro de Corretores'

    nome = models.CharField(verbose_name=u'Nome', max_length=255)
    # login = models.ForeignKey(
    #     User, verbose_name=u'Login', unique=True
    # )
    # senha = models.CharField(verbose_name=u'Senha', max_length=12)
    ativo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nome