# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Contato.telefone'
        db.alter_column(u'contato_contato', 'telefone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

    def backwards(self, orm):

        # Changing field 'Contato.telefone'
        db.alter_column(u'contato_contato', 'telefone', self.gf('django.db.models.fields.CharField')(default=1341341341, max_length=20))

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
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'contato.email': {
            'Meta': {'object_name': 'Email'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['contato']