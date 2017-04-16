# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_destination', models.CharField(max_length=2)),
                ('lat_destination', models.FloatField()),
                ('lng_destination', models.FloatField()),
                ('distance_km', models.FloatField()),
                ('destination_km2', models.IntegerField()),
                ('destination_language', models.CharField(max_length=3)),
                ('language_levenshtein_distance', models.FloatField()),
            ],
        ),
    ]
