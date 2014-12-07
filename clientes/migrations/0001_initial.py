# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EmailsRecebimento'
        db.create_table(u'clientes_emailsrecebimento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
        ))
        db.send_create_signal(u'clientes', ['EmailsRecebimento'])

        # Adding model 'PreCadastroCliente'
        db.create_table(u'clientes_precadastrocliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('data_nascimento', self.gf('django.db.models.fields.DateField')(max_length=255)),
            ('data_cadastro', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'clientes', ['PreCadastroCliente'])

        # Adding model 'CadastroCliente'
        db.create_table(u'clientes_cadastrocliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pre_cadastro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.PreCadastroCliente'], null=True, blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('data_nascimento', self.gf('django.db.models.fields.DateField')(max_length=255)),
            ('data_cadastro', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('rg', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cpf', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('endereco', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cidade', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('estado_civil', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=255)),
            ('profissao', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=255)),
            ('nome_conjuge', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('endereco_conjuge', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('telefone_conjuge', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('celular_conjuge', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('data_nascimento_conjuge', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('rg_conjuge', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cpf_conjuge', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('profissao_conjuge', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=255, null=True, blank=True)),
            ('faixa_salarial', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('filhos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('qtde_filhos', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=5, null=True, blank=True)),
        ))
        db.send_create_signal(u'clientes', ['CadastroCliente'])


    def backwards(self, orm):
        # Deleting model 'EmailsRecebimento'
        db.delete_table(u'clientes_emailsrecebimento')

        # Deleting model 'PreCadastroCliente'
        db.delete_table(u'clientes_precadastrocliente')

        # Deleting model 'CadastroCliente'
        db.delete_table(u'clientes_cadastrocliente')


    models = {
        u'clientes.cadastrocliente': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'CadastroCliente'},
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'celular_conjuge': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cpf': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cpf_conjuge': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'data_cadastro': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_nascimento': ('django.db.models.fields.DateField', [], {'max_length': '255'}),
            'data_nascimento_conjuge': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'endereco_conjuge': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'estado_civil': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '255'}),
            'faixa_salarial': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'filhos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nome_conjuge': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pre_cadastro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.PreCadastroCliente']", 'null': 'True', 'blank': 'True'}),
            'profissao': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '255'}),
            'profissao_conjuge': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'qtde_filhos': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rg_conjuge': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefone_conjuge': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'clientes.emailsrecebimento': {
            'Meta': {'ordering': "('id',)", 'object_name': 'EmailsRecebimento'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'clientes.precadastrocliente': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'PreCadastroCliente'},
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'data_cadastro': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_nascimento': ('django.db.models.fields.DateField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['clientes']