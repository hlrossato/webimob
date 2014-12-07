# -*- coding: utf-8 -*-

from django.db import models
from utils import util as U


class Banner(models.Model):

    class Meta:
        ordering = ('ordem', 'titulo')
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    titulo = models.CharField(verbose_name=u'Titulo do Banner', max_length=255)
    imagem = models.ImageField(
        verbose_name=u'Imagem', upload_to=U.rename_file_and_upload_to,
        max_length=255, help_text='Tamanho mínimo do banner: 1920x470'
    )
    link = models.URLField(
        verbose_name=u'Link do Banner', blank=True, null=True, max_length=255
    )
    ordem = models.PositiveIntegerField(
        verbose_name='Ordenação', blank=True, null=True
    )
    ativo = models.BooleanField(default=True)

    def thumb_display(self):
        from sorl.thumbnail import get_thumbnail

        try:
            foto = get_thumbnail(
                self.imagem, '100x60', quality=90, crop="center",
                upscale="true"
            )
            return '<img src="%s" >' % foto.url
        except:
            return 'Sem Foto'

    thumb_display.allow_tags = True
    thumb_display.is_safe = True
    thumb_display.short_description = u'Imagem'

    def __unicode__(self):
        return self.titulo
