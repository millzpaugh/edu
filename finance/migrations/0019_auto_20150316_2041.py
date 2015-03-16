# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0018_school_highlighted'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='highlighted',
            field=models.TextField(default=datetime.datetime(2015, 3, 16, 20, 41, 16, 809006, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='highlighted',
            field=models.TextField(default=datetime.datetime(2015, 3, 16, 20, 41, 26, 433537, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
