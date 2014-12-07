# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CadastroEmpreendimento.implantacao'
        db.alter_column(u'empreendimentos_cadastroempreendimento', 'implantacao', self.gf('sorl.thumbnail.fields.ImageField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'CadastroEmpreendimento.implantacao'
        db.alter_column(u'empreendimentos_cadastroempreendimento', 'implantacao', self.gf('django.db.models.fields.files.ImageField')(max_length=255))

    models = {
        u'empreendimentos.cadastroempreendimento': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'CadastroEmpreendimento'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'descricao': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'destaque': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ficha_tecnica': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantacao': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '255'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'metragem': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '255'})
        },
        u'empreendimentos.cadastrounidade': {
            'Meta': {'ordering': "('andar',)", 'object_name': 'CadastroUnidade'},
            'andar': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '255'}),
            'descricao': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'empreendimento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empreendimentos.CadastroEmpreendimento']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metragem': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'possui_suite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'qtde_banheiros': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '25'}),
            'qtde_quartos': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '25'}),
            'qtde_suites': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '255'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'empreendimentos.foto': {
            'Meta': {'ordering': "('legenda',)", 'object_name': 'Foto'},
            'empreendimento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empreendimentos.CadastroEmpreendimento']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'legenda': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'empreendimentos.fotosunidade': {
            'Meta': {'ordering': "('legenda',)", 'object_name': 'FotosUnidade'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'legenda': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ordem': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'unidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empreendimentos.CadastroUnidade']"})
        }
    }

    complete_apps = ['empreendimentos']