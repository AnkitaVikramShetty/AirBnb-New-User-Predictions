# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trial_predictions', '0007_auto_20170415_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='countries',
            name='destination_km2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='countries',
            name='distance_km',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='countries',
            name='language_levenshtein_distance',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='countries',
            name='lat_destination',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='countries',
            name='lng_destination',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test_users',
            name='age',
            field=models.IntegerField(blank=True, default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='train_users_2',
            name='age',
            field=models.IntegerField(blank=True, default=-1),
            preserve_default=False,
        ),
    ]
