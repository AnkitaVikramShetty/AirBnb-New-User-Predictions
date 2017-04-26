# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict_app', '0006_remove_train_users_2_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='age_gender_bkts',
            name='population_in_thousands',
        ),
        migrations.RemoveField(
            model_name='age_gender_bkts',
            name='year',
        ),
        migrations.RemoveField(
            model_name='countries',
            name='distance_km',
        ),
        migrations.RemoveField(
            model_name='countries',
            name='language_levenshtein_distance',
        ),
        migrations.RemoveField(
            model_name='countries',
            name='lat_destination',
        ),
        migrations.RemoveField(
            model_name='countries',
            name='lng_destination',
        ),
        migrations.RemoveField(
            model_name='sessions',
            name='secs_elapsed',
        ),
        migrations.RemoveField(
            model_name='test_users',
            name='age',
        ),
        migrations.RemoveField(
            model_name='test_users',
            name='signup_flow',
        ),
        migrations.RemoveField(
            model_name='train_users_2',
            name='signup_flow',
        ),
    ]
