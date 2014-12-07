# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Banner.link'
        db.add_column(u'banners_banner', 'link',
                      self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Banner.link'
        db.delete_column(u'banners_banner', 'link')


    models = {
        u'banners.banner': {
            'Meta': {'ordering': "('ordem', 'titulo')", 'object_name': 'Banner'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ordem': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['banners']