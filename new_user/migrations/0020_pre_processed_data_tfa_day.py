# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0019_remove_pre_processed_data_tfa_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='pre_processed_data',
            name='tfa_day',
            field=models.CharField(default=0, max_length=18),
            preserve_default=False,
        ),
    ]
