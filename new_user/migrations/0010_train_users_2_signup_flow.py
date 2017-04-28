# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0009_auto_20170426_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='train_users_2',
            name='signup_flow',
            field=models.FloatField(null=True),
        ),
    ]
