# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0015_auto_20170428_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pre_processed_data',
            name='id',
            field=models.CharField(serialize=False, max_length=50, primary_key=True),
        ),
    ]
