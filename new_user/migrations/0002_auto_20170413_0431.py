# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='age_gender_bkts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('age_bucket', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='sessions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('action', models.CharField(max_length=50)),
                ('action_type', models.CharField(max_length=50, blank=True)),
                ('action_detail', models.CharField(max_length=50, blank=True)),
                ('device_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='test_users',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('date_account_created', models.CharField(max_length=50, blank=True)),
                ('timestamp_first_active', models.CharField(max_length=6)),
                ('date_first_booking', models.CharField(max_length=50, blank=True)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField(blank=True)),
                ('signup_method', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=3)),
                ('affiliate_channel', models.CharField(max_length=15)),
                ('affiliate_provider', models.CharField(max_length=15)),
                ('first_affiliate_tracked', models.CharField(max_length=15, blank=True)),
                ('signup_app', models.CharField(max_length=15)),
                ('first_device_type', models.CharField(max_length=15)),
                ('first_browser', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='train_users_2',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('date_account_created', models.CharField(max_length=50, blank=True)),
                ('timestamp_first_active', models.CharField(max_length=6)),
                ('date_first_booking', models.CharField(max_length=50, blank=True)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField(blank=True)),
                ('signup_method', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=3)),
                ('affiliate_channel', models.CharField(max_length=15)),
                ('affiliate_provider', models.CharField(max_length=15)),
                ('first_affiliate_tracked', models.CharField(max_length=15, blank=True)),
                ('signup_app', models.CharField(max_length=15)),
                ('first_device_type', models.CharField(max_length=15)),
                ('first_browser', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='countries',
            name='id',
        ),
        migrations.AlterField(
            model_name='countries',
            name='country_destination',
            field=models.CharField(primary_key=True, max_length=2, serialize=False),
        ),
        migrations.AddField(
            model_name='train_users_2',
            name='country_destination',
            field=models.ForeignKey(to='new_user.countries'),
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
