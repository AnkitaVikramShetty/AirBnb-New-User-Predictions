# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0020_pre_processed_data_tfa_day'),
    ]

    operations = [
        migrations.DeleteModel(
            name='pre_processed_data',
        ),
    ]
