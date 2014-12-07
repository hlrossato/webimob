# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Banner'
        db.create_table(u'banners_banner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('imagem', self.gf('django.db.models.fields.files.ImageField')(max_length=255)),
            ('ordem', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'banners', ['Banner'])


    def backwards(self, orm):
        # Deleting model 'Banner'
        db.delete_table(u'banners_banner')


    models = {
        u'banners.banner': {
            'Meta': {'ordering': "('ordem', 'titulo')", 'object_name': 'Banner'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'ordem': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['banners']