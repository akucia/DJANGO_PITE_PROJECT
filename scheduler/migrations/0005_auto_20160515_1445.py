# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_remove_surveyuser_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyuser',
            name='sign_in_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
