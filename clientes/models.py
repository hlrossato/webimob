# -*- coding: utf-8 -*-

from django.db import models
from localflavor.br.br_states import STATE_CHOICES
from utils import util as U


class EmailsRecebimento(models.Model):

    class Meta:
        ordering = ('id', )
        verbose_name = 'Emails para Recebimento'
        verbose_name_plural = 'Emails para Recebimento'

    email = models.EmailField(verbose_name=u'Email', max_length=255)

    def __unicode__(self):
        return self.email


class PreCadastroCliente(models.Model):

    class Meta:
        ordering = ('nome', )
        verbose_name = u'Pré-Cadastro Cliente'
        verbose_name_plural = u'Pré-Cadastro Clientes'

    nome = models.CharField(verbose_name=u'Nome', max_length=255)
    email = models.EmailField(verbose_name=u'Email', max_length=255)
    telefone = models.CharField(
        verbose_name=u'Telefone', max_length=30, help_text='(99) 9999-9999'
    )
    celular = models.CharField(
        verbose_name=u'Celular', max_length=30, help_text='(99) 99999-9999',
        blank=True, null=True
    )
    data_nascimento = models.DateField(
        verbose_name=u'Data de Nascimento', max_length=255
    )
    data_cadastro = models.DateField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.nome


class CadastroCliente(models.Model):

    class Meta:
        ordering = ('nome', )
        verbose_name = u'Cadastro Cliente'
        verbose_name_plural = u'Cadastro Clientes'

    pre_cadastro = models.ForeignKey(
        PreCadastroCliente, blank=True, null=True, default=None
    )
    nome = models.CharField(verbose_name=u'Nome', max_length=255)
    email = models.EmailField(verbose_name=u'Email', max_length=255)
    telefone = models.CharField(
        verbose_name=u'Telefone', max_length=30, help_text='(99) 9999-9999'
    )
    celular = models.CharField(
        verbose_name=u'Celular', max_length=30, help_text='(99) 99999-9999',
        blank=True, null=True
    )
    data_nascimento = models.DateField(
        verbose_name=u'Data de Nascimento', max_length=255, auto_now=False
    )
    data_cadastro = models.DateField(auto_now_add=True, editable=False)    
    rg = models.CharField(verbose_name=u'RG', max_length=255)
    cpf = models.CharField(verbose_name=u'CPF', max_length=255)
    endereco = models.CharField(verbose_name=u'Endereço', max_length=255)
    cidade = models.CharField(verbose_name=u'Cidade', max_length=255)
    estado = models.CharField(
        verbose_name=u'Estado', choices=STATE_CHOICES, max_length=2
    )
    estado_civil = models.PositiveIntegerField(
        verbose_name=u'Estado Civil', max_length=255, choices=U.ESTADO_CIVIL
    )
    profissao = models.PositiveIntegerField(
        verbose_name=u'Profissão', max_length=255, choices=U.PROFISSOES
    )
    nome_conjuge = models.CharField(
        verbose_name=u'Nome do Conjugê', max_length=255, blank=True, null=True
    )
    endereco_conjuge = models.CharField(
        verbose_name=u'Endereço do Conjugê', max_length=255, blank=True, 
        null=True
    )
    telefone_conjuge = models.CharField(
        verbose_name=u'Telefone Conjugê', max_length=30,
        help_text='(99) 9999-9999', blank=True, null=True
    )
    celular_conjuge = models.CharField(
        verbose_name=u'Celular Conjugê', max_length=30,
        help_text='(99) 99999-9999', blank=True, null=True
    )
    data_nascimento_conjuge = models.DateField(
        verbose_name=u'Data Nascimento Conjugê', blank=True, null=True
    )
    rg_conjuge = models.CharField(
        verbose_name=u'RG Conjugê', max_length=255, blank=True, null=True
    )
    cpf_conjuge = models.CharField(
        verbose_name=u'CPF Conjugê', max_length=255, blank=True, null=True
    )
    profissao_conjuge = models.IntegerField(
        verbose_name=u'Profissão Conjugê', max_length=255, choices=U.PROFISSOES,
        blank=True, null=True,
    )
    faixa_salarial = models.CharField(
        verbose_name=u'Faixa Salarial Total', max_length=255
    )
    filhos = models.NullBooleanField(verbose_name=u'Possui Filhos?')
    qtde_filhos = models.IntegerField(
        verbose_name=u'Quantos Filhos', max_length=5, blank=True, null=True
    )

    def __unicode__(self):
        return self.nome