# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Image'
        db.delete_table(u'draw_image')

        # Removing M2M table for field authors on 'Image'
        db.delete_table(db.shorten_name(u'draw_image_authors'))

        # Adding model 'Drawing'
        db.create_table(u'draw_drawing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('local_path', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'draw', ['Drawing'])

        # Adding M2M table for field author on 'Drawing'
        m2m_table_name = db.shorten_name(u'draw_drawing_author')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('drawing', models.ForeignKey(orm[u'draw.drawing'], null=False)),
            ('user', models.ForeignKey(orm[u'draw.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['drawing_id', 'user_id'])


    def backwards(self, orm):
        # Adding model 'Image'
        db.create_table(u'draw_image', (
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'draw', ['Image'])

        # Adding M2M table for field authors on 'Image'
        m2m_table_name = db.shorten_name(u'draw_image_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('image', models.ForeignKey(orm[u'draw.image'], null=False)),
            ('user', models.ForeignKey(orm[u'draw.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['image_id', 'user_id'])

        # Deleting model 'Drawing'
        db.delete_table(u'draw_drawing')

        # Removing M2M table for field author on 'Drawing'
        db.delete_table(db.shorten_name(u'draw_drawing_author'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'draw.drawing': {
            'Meta': {'object_name': 'Drawing'},
            'author': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'author'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['draw.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_path': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'draw.user': {
            'Meta': {'object_name': 'User'},
            'about': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['draw']