# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_auto_20150312_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='sector',
            field=models.CharField(default=None, max_length=30, choices=[(b'public', b'Public'), (b'private-nonprofit', b'Private-Nonprofit'), (b'proprietary', b'Proprietary'), (b'foreign_private', b'Foreign Private'), (b'foreign_public', b'Foreign Public')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='zip',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
