# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DomainName'
        db.create_table(u'domains_domainname', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('expiration_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('registrar', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'domains', ['DomainName'])


    def backwards(self, orm):
        # Deleting model 'DomainName'
        db.delete_table(u'domains_domainname')


    models = {
        u'domains.domainname': {
            'Meta': {'object_name': 'DomainName'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'registrar': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['domains']