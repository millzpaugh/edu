# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='school_type',
        ),
        migrations.AlterField(
            model_name='school',
            name='sector',
            field=models.CharField(default=None, max_length=2, choices=[(b'public', b'Public'), (b'non_profit', b'Private-Nonprofit'), (b'private', b'Proprietary')]),
            preserve_default=True,
        ),
    ]
