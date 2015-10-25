# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffnetworks', '0003_auto_20151025_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='asn',
            field=models.ForeignKey(to='ffnetworks.ASN', blank=True, null=True, related_name='nodes'),
        ),
    ]
