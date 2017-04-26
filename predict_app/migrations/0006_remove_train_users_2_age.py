# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict_app', '0005_remove_countries_destination_km2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train_users_2',
            name='age',
        ),
    ]
