# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict_app', '0010_pre_processed_data_results'),
    ]

    operations = [
        migrations.DeleteModel(
            name='pre_processed_data',
        ),
    ]
