# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0017_pre_processed_data_date_first_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pre_processed_data',
            name='date_first_booking',
        ),
        migrations.AlterField(
            model_name='pre_processed_data',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
