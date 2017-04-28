# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0012_auto_20170428_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_users',
            name='first_affiliate_tracked',
            field=models.CharField(null=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='train_users_2',
            name='first_affiliate_tracked',
            field=models.CharField(null=True, max_length=15),
        ),
    ]
