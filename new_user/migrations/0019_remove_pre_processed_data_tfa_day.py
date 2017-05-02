# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0018_auto_20170501_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pre_processed_data',
            name='tfa_day',
        ),
    ]
