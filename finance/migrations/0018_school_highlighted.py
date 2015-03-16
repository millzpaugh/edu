# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0017_auto_20150316_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='highlighted',
            field=models.TextField(default=datetime.datetime(2015, 3, 16, 20, 16, 26, 822621, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
