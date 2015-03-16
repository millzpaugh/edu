# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_auto_20150313_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='number_of_disbursements',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
