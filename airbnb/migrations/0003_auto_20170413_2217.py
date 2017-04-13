# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airbnb', '0002_auto_20170413_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train_users_2',
            name='age',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
