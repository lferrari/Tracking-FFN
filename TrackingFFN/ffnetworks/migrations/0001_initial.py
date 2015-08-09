# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ASN',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('number', models.CharField(verbose_name='ASN Number', max_length=50)),
                ('as_name', models.CharField(verbose_name='AS Name', max_length=200)),
                ('country', models.CharField(verbose_name='Country', max_length='2')),
                ('domain', models.CharField(verbose_name='Domain URL', max_length='50')),
                ('isp', models.CharField(verbose_name='ISP Name', max_length='200')),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('url', models.URLField(verbose_name='URL')),
                ('submit_date', models.DateField(verbose_name='Submit Date', auto_now_add=True)),
                ('last_seen', models.DateField(verbose_name='Last Seen')),
                ('live', models.BooleanField(verbose_name='Live')),
                ('track', models.BooleanField(verbose_name='Track')),
                ('domain_type', models.CharField(choices=[(1, 'Single-Flux Networks'), (2, 'Double-Flux Networks')], verbose_name='Fast Flux Network Type', max_length='2', default='1')),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('date_detected', models.DateField(verbose_name='Date Detected', auto_now_add=True)),
                ('dns_registry_type', models.CharField(choices=[(1, 'A'), (2, 'NS')], verbose_name='DNS Registry Type', max_length='2')),
                ('asn', models.ForeignKey(to='ffnetworks.ASN', related_name='nodes')),
                ('domain', models.ForeignKey(to='ffnetworks.Domain', related_name='nodes')),
            ],
        ),
    ]
