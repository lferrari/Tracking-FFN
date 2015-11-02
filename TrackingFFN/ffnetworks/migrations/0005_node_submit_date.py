# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ffnetworks', '0004_auto_20151025_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='submit_date',
            field=models.DateField(auto_now_add=True, verbose_name='Submit Date', default=datetime.datetime(2015, 11, 1, 19, 58, 17, 584724, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
