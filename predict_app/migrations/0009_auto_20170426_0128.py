# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict_app', '0008_auto_20170424_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_users',
            name='signup_flow',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='test_users',
            name='age',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='test_users',
            name='timestamp_first_active',
            field=models.CharField(max_length=18),
        ),
    ]
