# -*- coding: utf-8 -*-

from django.db import models
from localflavor.br.br_states import STATE_CHOICES
from tinymce import models as tinymce_models
from utils import util as U


class CadastroEmpreendimento(models.Model):

    class Meta:
        ordering = ('nome', )
        verbose_name = 'Cadastro de Empreendimento'
        verbose_name_plural = 'Cadastro de Empreendimentos'

    nome = models.CharField(verbose_name=u'Nome', max_length=255)
    slug = models.SlugField(
        verbose_name=u'Slug/URL', max_length=255, unique=True,
        help_text="Preenchido automaticamente, não editar."
    )
    destaque = models.BooleanField(
        verbose_name=u'Destaque', default=False,
        help_text=u'Marque esta opção para este imóvel aparecer na Home do site'
    )
    descricao = tinymce_models.HTMLField(
        verbose_name=u'Descrição', null=True, blank=True
    )
    ficha_tecnica = tinymce_models.HTMLField(
        verbose_name=u'Ficha Técnica', null=True, blank=True
    )
    latitude = models.CharField(verbose_name=u'Latitude', max_length=255)
    longitude = models.CharField(verbose_name=u'Longitude', max_length=255)
    endereco = models.CharField(verbose_name=u'Endereço', max_length=255)
    bairro = models.CharField(verbose_name=u'Bairro', max_length=255)
    cidade = models.CharField(verbose_name=u'Cidade', max_length=255)
    estado = models.CharField(
        verbose_name=u'Estado', max_length=255, choices=STATE_CHOICES
    )
    implantacao = models.ImageField(
        verbose_name=u'Implantação', max_length=255,
        upload_to=U.rename_file_and_upload_to,
        help_text=u'Insirir a imagem da implantação do empreendimento'
    )
    metragem = tinymce_models.HTMLField(
        verbose_name=u'Metragem', blank=True, null=True
    )
    status = models.PositiveIntegerField(
        verbose_name=u'Status', max_length=255, choices=U.STATUS_CHOICES
    )
    ativo = models.BooleanField(verbose_name=u'Ativo', default=True)

    def imagemAdmin(self):
        from sorl.thumbnail import get_thumbnail

        if self.implantacao:
            try:
                im = get_thumbnail(self.implantacao, '100x60', quality=80)
                return '<img src="%s" />' % im.url
            except:
                return 'Imagem Corrompida'
        return 'Sem Imagem'

    imagemAdmin.is_safe = True
    imagemAdmin.allow_tags = True
    imagemAdmin.short_description = u'Imagem'

    def get_first_image(self):
        imagem = Foto.objects.filter(empreendimento=self)

        if imagem:
            imagem = imagem[0]

        return imagem

    def __unicode__(self):
        return self.nome


class Foto(models.Model):

    class Meta:
        ordering = ('legenda', )
        verbose_name = 'Foto do Empreendimento'
        verbose_name_plural = 'Fotos do Empreendimento'

    empreendimento = models.ForeignKey(CadastroEmpreendimento)
    legenda = models.CharField(verbose_name=u'Legenda da Foto', max_length=255)
    imagem = models.ImageField(
        verbose_name=u'Imagem', max_length=255,
        upload_to=U.rename_file_and_upload_to
    )

    def imagemAdmin(self):
        from sorl.thumbnail import get_thumbnail

        if self.imagem:
            try:
                im = get_thumbnail(self.imagem, '100x60', quality=80)
                return '<img src="%s" />' % im.url
            except:
                return 'Imagem Corrompida'
        return 'Sem Imagem'

    imagemAdmin.is_safe = True
    imagemAdmin.allow_tags = True
    imagemAdmin.short_description = u'Imagem'

    def __unicode__(self):
        return self.legenda


class CadastroUnidade(models.Model):

    class Meta:
        ordering = ('andar', )
        verbose_name = 'Cadastro de Unidade'
        verbose_name_plural = 'Cadastro de Unidades'

    empreendimento = models.ForeignKey(CadastroEmpreendimento)
    status = models.PositiveIntegerField(
        verbose_name=u'Status da Unidade', max_length=255, 
        choices=U.STATUS_UNIDADES, default=1
    )
    titulo = models.CharField(verbose_name=u'Titulo', max_length=255,
                              help_text=u"""Titulo para unidade para questões de organização"""
                              )
    slug = models.SlugField(
        verbose_name=u'Slug/URL', max_length=255, unique=True,
        help_text="Preenchido automaticamente, não editar."
    )
    andar = models.PositiveIntegerField(verbose_name=u'Andar', max_length=255)
    metragem = tinymce_models.HTMLField(
        verbose_name=u'Metragem', blank=True, null=True
    )
    descricao = tinymce_models.HTMLField(
        verbose_name=u'Descrição', null=True, blank=True
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
        foto_destaque = FotosUnidade.objects.filter(unidade=self, ordem=1)

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

    def __unicode__(self):
        return self.titulo


class Plantas(models.Model):

    class Meta:
        ordering = ('legenda', )
        verbose_name = 'Planta'
        verbose_name_plural = 'Plantas'

    empreendimento = models.ForeignKey(CadastroEmpreendimento)
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


class FotosUnidade(models.Model):

    class Meta:
        ordering = ('legenda', )
        verbose_name = 'Foto da Unidade'
        verbose_name_plural = 'Fotos das Unidades'

    unidade = models.ForeignKey(CadastroUnidade)
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
