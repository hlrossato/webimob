# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CadastroCorretor.senha'
        db.delete_column(u'corretores_cadastrocorretor', 'senha')

        # Deleting field 'CadastroCorretor.login'
        db.delete_column(u'corretores_cadastrocorretor', 'login_id')


    def backwards(self, orm):
        # Adding field 'CadastroCorretor.senha'
        db.add_column(u'corretores_cadastrocorretor', 'senha',
                      self.gf('django.db.models.fields.CharField')(default='teste', max_length=12),
                      keep_default=False)

        # Adding field 'CadastroCorretor.login'
        db.add_column(u'corretores_cadastrocorretor', 'login',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='teste', to=orm['auth.User'], unique=True),
                      keep_default=False)


    models = {
        u'corretores.cadastrocorretor': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'CadastroCorretor'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['corretores']