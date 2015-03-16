# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_auto_20150311_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='grant_type',
            field=models.CharField(default=None, max_length=30, choices=[(b'pell', b'Pell Grant'), (b'teach', b'Teach Grant Program'), (b'iraq_afghan', b'Iraq Afghanistan Grant Program')]),
            preserve_default=True,
        ),
    ]
