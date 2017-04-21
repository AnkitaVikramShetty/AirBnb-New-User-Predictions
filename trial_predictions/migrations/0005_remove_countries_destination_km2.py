# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trial_predictions', '0004_auto_20170413_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countries',
            name='destination_km2',
        ),
    ]
