# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trial_prediction_2', '0002_auto_20170413_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='destination_km2',
            field=models.FloatField(),
        ),
    ]
