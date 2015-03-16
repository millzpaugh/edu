# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0009_auto_20150313_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_type',
            field=models.CharField(default=None, max_length=80, choices=[(b'dl_sub_ugrad', b'Direct Loan Subsidized Undergraduate'), (b'dl_unsub_ugrad', b'Direct Loan Unsubsidized Undergraduate'), (b'dl_sub_grad', b'Direct Loan Subsidized Graduate'), (b'dl_unsub_grad', b'Direct Loan Unsubsidized Graduate'), (b'dl_parent_plus', b'Direct Loan Parent Plus'), (b'dl_grad_plus', b'Direct Loan Grad Plus')]),
            preserve_default=True,
        ),
    ]
