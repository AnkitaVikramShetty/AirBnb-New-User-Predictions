# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='age_gender_bkts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('age_bucket', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='countries',
            fields=[
                ('country_destination', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('lat_destination', models.FloatField()),
                ('lng_destination', models.FloatField()),
                ('distance_km', models.FloatField()),
                ('destination_km2', models.FloatField(default=0.0)),
                ('destination_language', models.CharField(max_length=3)),
                ('language_levenshtein_distance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='sessions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('action', models.CharField(max_length=50)),
                ('action_type', models.CharField(blank=True, max_length=50)),
                ('action_detail', models.CharField(blank=True, max_length=50)),
                ('device_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='test_users',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date_account_created', models.CharField(blank=True, max_length=50)),
                ('timestamp_first_active', models.CharField(max_length=6)),
                ('date_first_booking', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField(blank=True)),
                ('signup_method', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=3)),
                ('affiliate_channel', models.CharField(max_length=15)),
                ('affiliate_provider', models.CharField(max_length=15)),
                ('first_affiliate_tracked', models.CharField(blank=True, max_length=15)),
                ('signup_app', models.CharField(max_length=15)),
                ('first_device_type', models.CharField(max_length=15)),
                ('first_browser', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='train_users_2',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date_account_created', models.CharField(blank=True, max_length=50)),
                ('timestamp_first_active', models.CharField(max_length=6)),
                ('date_first_booking', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField(blank=True)),
                ('signup_method', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=3)),
                ('affiliate_channel', models.CharField(max_length=15)),
                ('affiliate_provider', models.CharField(max_length=15)),
                ('first_affiliate_tracked', models.CharField(blank=True, max_length=15)),
                ('signup_app', models.CharField(max_length=15)),
                ('first_device_type', models.CharField(max_length=15)),
                ('first_browser', models.CharField(max_length=15)),
                ('country_destination', models.ForeignKey(to='new_user.countries')),
            ],
        ),
        migrations.AddField(
            model_name='sessions',
            name='user_id',
            field=models.ForeignKey(to='new_user.train_users_2'),
        ),
        migrations.AddField(
            model_name='age_gender_bkts',
            name='country_destination',
            field=models.ForeignKey(to='new_user.countries'),
        ),
    ]
