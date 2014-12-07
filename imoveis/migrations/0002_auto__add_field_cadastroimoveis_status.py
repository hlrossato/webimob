# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CadastroImoveis.status'
        db.add_column(u'imoveis_cadastroimoveis', 'status',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CadastroImoveis.status'
        db.delete_column(u'imoveis_cadastroimoveis', 'status')


    models = {
        u'imoveis.cadastroimoveis': {
            'Meta': {'ordering': "('titulo',)", 'object_name': 'CadastroImoveis'},
            'andar': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'descricao': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'destaque': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'finalidade': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'metragem': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'possui_suite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'qtde_banheiros': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '25'}),
            'qtde_quartos': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '25'}),
            'qtde_suites': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'max_length': '255'}),
            'tipo_imovel': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tipo_transacao': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'imoveis.fotosimoveis': {
            'Meta': {'ordering': "('legenda',)", 'object_name': 'FotosImoveis'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'imovel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['imoveis.CadastroImoveis']"}),
            'legenda': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ordem': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['imoveis']