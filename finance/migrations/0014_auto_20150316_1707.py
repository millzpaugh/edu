# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0013_auto_20150316_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='sector',
            field=models.CharField(default=None, max_length=30, choices=[(b'public', b'Public'), (b'private', b'Private'), (b'private-nonprofit', b'Private-Nonprofit'), (b'proprietary', b'Proprietary'), (b'foreign private', b'Foreign Private'), (b'foreign public', b'Foreign Public')]),
            preserve_default=True,
        ),
    ]
