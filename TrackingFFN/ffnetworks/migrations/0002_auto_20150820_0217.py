# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffnetworks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asn',
            name='full_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asn',
            name='as_name',
            field=models.CharField(verbose_name='AS Name', null=True, max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='asn',
            name='domain',
            field=models.CharField(verbose_name='Domain URL', null=True, max_length='50', blank=True),
        ),
        migrations.AlterField(
            model_name='asn',
            name='isp',
            field=models.CharField(verbose_name='ISP Name', null=True, max_length='200', blank=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='domain_type',
            field=models.CharField(choices=[('SINGLE', 'Single-Flux Networks'), ('DOUBLE', 'Double-Flux Networks')], verbose_name='Fast Flux Network Type', max_length=6, default='SINGLE'),
        ),
    ]
