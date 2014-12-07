# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Email'
        db.create_table(u'contato_email', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
        ))
        db.send_create_signal(u'contato', ['Email'])

        # Adding model 'Assunto'
        db.create_table(u'contato_assunto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'contato', ['Assunto'])

        # Adding M2M table for field email_assunto on 'Assunto'
        m2m_table_name = db.shorten_name(u'contato_assunto_email_assunto')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('assunto', models.ForeignKey(orm[u'contato.assunto'], null=False)),
            ('email', models.ForeignKey(orm[u'contato.email'], null=False))
        ))
        db.create_unique(m2m_table_name, ['assunto_id', 'email_id'])

        # Adding model 'Contato'
        db.create_table(u'contato_contato', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('assunto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contato.Assunto'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('mensagem', self.gf('django.db.models.fields.TextField')()),
            ('data', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'contato', ['Contato'])


    def backwards(self, orm):
        # Deleting model 'Email'
        db.delete_table(u'contato_email')

        # Deleting model 'Assunto'
        db.delete_table(u'contato_assunto')

        # Removing M2M table for field email_assunto on 'Assunto'
        db.delete_table(db.shorten_name(u'contato_assunto_email_assunto'))

        # Deleting model 'Contato'
        db.delete_table(u'contato_contato')


    models = {
        u'contato.assunto': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'Assunto'},
            'email_assunto': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['contato.Email']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'contato.contato': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'Contato'},
            'assunto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contato.Assunto']"}),
            'data': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mensagem': ('django.db.models.fields.TextField', [], {}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'contato.email': {
            'Meta': {'object_name': 'Email'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['contato']