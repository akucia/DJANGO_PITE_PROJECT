# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_auto_20160515_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyuser',
            name='telephone',
        ),
    ]
