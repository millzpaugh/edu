# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0015_auto_20150316_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='sector',
            field=models.CharField(default=None, max_length=30, choices=[(b'public', b'Public'), (b'private', b'Private'), (b'private-nonprofit', b'Private-Nonprofit'), (b'proprietary', b'Proprietary'), (b'foreign private', b'Foreign Private'), (b'foreign-private', b'Foreign Private'), (b'foreign public', b'Foreign Public'), (b'foreign-public', b'Foreign Public'), (b'foreign for-profit', b'Foreign For-Profit')]),
            preserve_default=True,
        ),
    ]
