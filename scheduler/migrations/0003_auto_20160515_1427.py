# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20160515_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyuser',
            name='telephone',
            field=models.CharField(max_length=15, blank=True),
        ),
    ]
