# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict_app', '0009_auto_20170426_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='pre_processed_data',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('affiliate_channel', models.CharField(max_length=15)),
                ('affiliate_provider', models.CharField(max_length=15)),
                ('age', models.FloatField(null=True)),
                ('first_affiliate_tracked', models.CharField(max_length=15, blank=True)),
                ('first_browser', models.CharField(max_length=15)),
                ('first_device_type', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('language', models.CharField(max_length=3)),
                ('signup_app', models.CharField(max_length=15)),
                ('signup_flow', models.FloatField(null=True)),
                ('signup_method', models.CharField(max_length=20)),
                ('dac_year', models.CharField(max_length=18)),
                ('dac_month', models.CharField(max_length=18)),
                ('dac_day', models.CharField(max_length=18)),
                ('tfa_year', models.CharField(max_length=18)),
                ('tfa_month', models.CharField(max_length=18)),
                ('tfa_day', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='results',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('results_id', models.CharField(max_length=50)),
                ('country_destination', models.CharField(max_length=50)),
            ],
        ),
    ]
