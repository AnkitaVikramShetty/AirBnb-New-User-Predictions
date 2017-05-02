# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0021_delete_pre_processed_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='pre_processed_data',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.FloatField(null=True)),
                ('signup_method', models.CharField(max_length=20)),
                ('signup_flow', models.FloatField(null=True)),
                ('language', models.CharField(max_length=3)),
                ('affiliate_channel', models.CharField(max_length=15)),
                ('affiliate_provider', models.CharField(max_length=15)),
                ('first_affiliate_tracked', models.CharField(null=True, max_length=15)),
                ('signup_app', models.CharField(max_length=15)),
                ('first_device_type', models.CharField(max_length=15)),
                ('first_browser', models.CharField(max_length=15)),
                ('dac_year', models.CharField(max_length=18)),
                ('dac_month', models.CharField(max_length=18)),
                ('dac_day', models.CharField(max_length=18)),
                ('tfa_year', models.CharField(max_length=18)),
                ('tfa_month', models.CharField(max_length=18)),
                ('tfa_day', models.CharField(max_length=18)),
            ],
        ),
    ]
