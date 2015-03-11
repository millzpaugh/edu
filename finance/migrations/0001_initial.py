# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grant_type', models.CharField(default=None, max_length=2, choices=[(b'pell', b'Pell Grant'), (b'teach', b'Teach Grant Program'), (b'iraq_afghan', b'Iraq Afghanistan Grant Program')])),
                ('recipients', models.IntegerField(null=True)),
                ('grant_money_disbursed', models.DecimalField(null=True, max_digits=30, decimal_places=2)),
                ('year', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loan_type', models.CharField(default=None, max_length=2, choices=[(b'dl_sub_ugrad', b'Direct Loan Subsidized Undergraduate'), (b'dl_unsub_ugrad', b'Direct Loan Unsubsidized Undergraduate'), (b'dl_sub_grad', b'Direct Loan Subsidized Graduate'), (b'dl_unsub_grad', b'Direct Loan Unsubsidized Graduate'), (b'dl_parent_plus', b'Direct Loan Parent Plus'), (b'dl_grad_plus', b'Direct Loan Grad Plus')])),
                ('recipients', models.IntegerField(null=True)),
                ('number_of_loans', models.IntegerField(null=True)),
                ('loan_money_originated', models.DecimalField(null=True, max_digits=30, decimal_places=2)),
                ('number_of_disbursements', models.IntegerField()),
                ('loan_money_disbursed', models.DecimalField(null=True, max_digits=30, decimal_places=2)),
                ('year', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.IntegerField(max_length=50)),
                ('sector', models.CharField(max_length=50)),
                ('school_type', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='loan',
            name='school_id',
            field=models.ForeignKey(to='finance.School'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grant',
            name='school_id',
            field=models.ForeignKey(to='finance.School'),
            preserve_default=True,
        ),
    ]
