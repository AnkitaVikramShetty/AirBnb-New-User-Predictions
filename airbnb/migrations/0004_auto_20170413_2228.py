# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airbnb', '0003_auto_20170413_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train_users_2',
            name='age',
            field=models.FloatField(blank=True),
        ),
    ]
