# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0002_auto_20170424_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_users',
            name='timestamp_first_active',
            field=models.CharField(max_length=18),
        ),
    ]
