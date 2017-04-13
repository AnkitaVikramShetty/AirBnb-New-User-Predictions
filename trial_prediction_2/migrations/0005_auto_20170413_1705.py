# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trial_prediction_2', '0004_auto_20170413_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train_users_2',
            name='age',
            field=models.IntegerField(blank=True),
        ),
    ]
