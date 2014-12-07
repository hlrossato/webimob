# -*- coding: utf-8 -*-

from django.db import models
from utils import util as U
from localflavor.br.br_states import STATE_CHOICES
from tinymce import models as tinymce_models


class CadastroImoveis(models.Model):

    class Meta:
        ordering = ('titulo', )
        verbose_name = 'Cadastro de Imóvel'
        verbose_name_plural = 'Cadastro de Imóveis'

    tipo_imovel = models.PositiveIntegerField(
        verbose_name=u'Tipo do Imóvel', choices=U.TIPO_IMOVEL
    )
    tipo_transacao = models.PositiveIntegerField(
        verbose_name=u'Tipo de Transação', choices=U.TIPO_TRANSACAO
    )
    finalidade = models.PositiveIntegerField(
        verbose_name=u'Finalidade do Imóvel', choices=U.FINALIDADE
    )
    titulo = models.CharField(verbose_name=u'Titulo', max_length=255)
    slug = models.SlugField(
        verbose_name=u'Slug/URL', max_length=255, unique=True,
        help_text="Preenchido automaticamente, não editar."
    )
    destaque = models.BooleanField(
        verbose_name=u'Destaque', default=False,
        help_text=u'Marque esta opção para este imóvel aparecer na Home do site'
    )
    ativo = models.BooleanField(default=True)
    status = models.PositiveIntegerField(
        verbose_name=u'Status da Unidade', max_length=255, 
        choices=U.STATUS_IMOVEIS, default=1
    )    
    descricao = tinymce_models.HTMLField(
        verbose_name=u'Descrição do Imóvel', null=True, blank=True
    )
    metragem = tinymce_models.HTMLField(
        verbose_name=u'Metragem', blank=True, null=True
    )
    andar = models.PositiveIntegerField(
        verbose_name=u'Andar', max_length=255, blank=True, null=True
    )
    latitude = models.CharField(verbose_name=u'Latitude', max_length=255)
    longitude = models.CharField(verbose_name=u'Longitude', max_length=255)
    endereco = models.CharField(verbose_name=u'Endereço', max_length=255)
    bairro = models.CharField(verbose_name=u'Bairro', max_length=255)
    cidade = models.CharField(verbose_name=u'Cidade', max_length=255)
    estado = models.CharField(
        verbose_name=u'Estado', max_length=255, choices=STATE_CHOICES
    )
    qtde_quartos = models.PositiveIntegerField(
        verbose_name=u'Quantidade de Quartos', max_length=25
    )
    qtde_banheiros = models.PositiveIntegerField(
        verbose_name=u'Quantidade de Banheiros', max_length=25
    )
    possui_suite = models.BooleanField(
        verbose_name=u'Possui Suite?', default=False,
        help_text=u"""Marcando esta opção, será necessário preencher o campo
        abaixo informando a quantidade de suites existentes""",
    )
    qtde_suites = models.PositiveIntegerField(
        verbose_name=u'Quantidade de Suites', max_length=3, blank=True,
        null=True, help_text=u"""Preencha esse campo somente quando o campo
        acima for preenchido previamente"""
    )

    def imagemAdmin(self):

        from sorl.thumbnail import get_thumbnail
        foto_destaque = FotosImoveis.objects.filter(imovel=self, ordem=1)

        if foto_destaque:
            foto_destaque = foto_destaque[0]
            try:
                im = get_thumbnail(foto_destaque.imagem, '100x60', quality=80)
                return '<img src="%s" />' % im.url
            except:
                return 'Imagem Corrompida'
        return 'Sem Imagem'
    imagemAdmin.is_safe = True
    imagemAdmin.allow_tags = True
    imagemAdmin.short_description = 'Imagem'        

    def get_first_image(self):
        imagem = FotosImoveis.objects.filter(imovel=self)

        if imagem:
            imagem = imagem[0]

        return imagem

    def __unicode__(self):
        return self.titulo


class FotosImoveis(models.Model):

    class Meta:
        ordering = ('legenda', )
        verbose_name = 'Foto do Imóvel'
        verbose_name_plural = 'Fotos dos Imóveis'

    imovel = models.ForeignKey(CadastroImoveis)
    legenda = models.CharField(verbose_name=u'Legenda da Foto', max_length=255)
    imagem = models.ImageField(
        verbose_name=u'Imagem', max_length=255,
        upload_to=U.rename_file_and_upload_to
    )
    ordem = models.PositiveIntegerField(
        verbose_name='Ordenação', blank=True, null=True
    )

    def __unicode__(self):
        return self.legenda
