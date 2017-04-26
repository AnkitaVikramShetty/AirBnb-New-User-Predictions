# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0005_auto_20170425_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_users',
            name='signup_flow',
            field=models.FloatField(null=True),
        ),
    ]
