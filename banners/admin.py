# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Banner


class BannerAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ordem', 'thumb_display')
    search_fields = ('titulo', )
    list_filter = ['ativo', ]
    save_on_top = True
    list_per_page = 20


admin.site.register(Banner, BannerAdmin)
