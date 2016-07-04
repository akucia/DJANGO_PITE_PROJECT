# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0008_auto_20160521_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
