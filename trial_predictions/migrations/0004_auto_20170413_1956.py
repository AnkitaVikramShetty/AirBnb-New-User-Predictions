# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trial_predictions', '0003_auto_20170413_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='age_gender_bkts',
            name='population_in_thousands',
            field=models.IntegerField(blank=True, null=True, default=0),
        ),
        migrations.AddField(
            model_name='age_gender_bkts',
            name='year',
            field=models.IntegerField(blank=True, null=True, default=0),
        ),
        migrations.AddField(
            model_name='sessions',
            name='secs_elapsed',
            field=models.IntegerField(blank=True, null=True, default=0),
        ),
        migrations.AddField(
            model_name='test_users',
            name='signup_flow',
            field=models.IntegerField(blank=True, null=True, default=0),
        ),
        migrations.AddField(
            model_name='train_users_2',
            name='signup_flow',
            field=models.IntegerField(blank=True, null=True, default=0),
        ),
        migrations.AlterField(
            model_name='countries',
            name='destination_km2',
            field=models.IntegerField(blank=True, null=True, default=0),
        ),
        migrations.AlterField(
            model_name='train_users_2',
            name='age',
            field=models.IntegerField(blank=True, null=True, default=0),
        ),
    ]
