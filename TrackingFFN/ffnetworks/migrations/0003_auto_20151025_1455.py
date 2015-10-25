# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffnetworks', '0002_auto_20150820_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='url',
            field=models.CharField(verbose_name='URL', max_length=50),
        ),
    ]
