# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0016_auto_20170501_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='pre_processed_data',
            name='date_first_booking',
            field=models.CharField(null=True, max_length=50),
        ),
    ]
