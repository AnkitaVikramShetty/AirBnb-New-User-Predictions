# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0011_auto_20170428_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pre_processed_data',
            name='first_affiliate_tracked',
            field=models.CharField(null=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='sessions',
            name='action_detail',
            field=models.CharField(null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='sessions',
            name='action_type',
            field=models.CharField(null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='test_users',
            name='date_account_created',
            field=models.CharField(null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='test_users',
            name='date_first_booking',
            field=models.CharField(null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='train_users_2',
            name='age',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='train_users_2',
            name='date_account_created',
            field=models.CharField(null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='train_users_2',
            name='date_first_booking',
            field=models.CharField(null=True, max_length=50),
        ),
    ]
