# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CadastroEmpreendimento'
        db.create_table(u'empreendimentos_cadastroempreendimento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
            ('destaque', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descricao', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('ficha_tecnica', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('endereco', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('bairro', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cidade', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('implantacao', self.gf('django.db.models.fields.files.ImageField')(max_length=255)),
            ('metragem', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=255)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'empreendimentos', ['CadastroEmpreendimento'])

        # Adding model 'Foto'
        db.create_table(u'empreendimentos_foto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empreendimento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empreendimentos.CadastroEmpreendimento'])),
            ('legenda', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('imagem', self.gf('django.db.models.fields.files.ImageField')(max_length=255)),
        ))
        db.send_create_signal(u'empreendimentos', ['Foto'])

        # Adding model 'CadastroUnidade'
        db.create_table(u'empreendimentos_cadastrounidade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empreendimento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empreendimentos.CadastroEmpreendimento'])),
            ('status', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=255)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
            ('andar', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=255)),
            ('metragem', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('descricao', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('qtde_quartos', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=25)),
            ('qtde_banheiros', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=25)),
            ('possui_suite', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('qtde_suites', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=3, null=True, blank=True)),
        ))
        db.send_create_signal(u'empreendimentos', ['CadastroUnidade'])

        # Adding model 'FotosUnidade'
        db.create_table(u'empreendimentos_fotosunidade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empreendimentos.CadastroUnidade'])),
            ('legenda', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('imagem', self.gf('django.db.models.fields.files.ImageField')(max_length=255)),
            ('ordem', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'empreendimentos', ['FotosUnidade'])


    def backwards(self, orm):
        # Deleting model 'CadastroEmpreendimento'
        db.delete_table(u'empreendimentos_cadastroempreendimento')

        # Deleting model 'Foto'
        db.delete_table(u'empreendimentos_foto')

        # Deleting model 'CadastroUnidade'
        db.delete_table(u'empreendimentos_cadastrounidade')

        # Deleting model 'FotosUnidade'
        db.delete_table(u'empreendimentos_fotosunidade')


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
            'implantacao': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
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