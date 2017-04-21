# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trial_predictions', '0002_auto_20170413_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_users',
            name='age',
            field=models.IntegerField(blank=True, null=True, default=0),
        ),
    ]
