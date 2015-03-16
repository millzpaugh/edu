# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_auto_20150312_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='sector',
            field=models.CharField(default=None, max_length=30, choices=[(b'public', b'Public'), (b'private-nonprofit', b'Private-Nonprofit'), (b'proprietary', b'Proprietary')]),
            preserve_default=True,
        ),
    ]
