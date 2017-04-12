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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('country_destination', models.CharField(max_length=2)),
                ('lat_destination', models.FloatField()),
                ('lng_destination', models.FloatField()),
                ('distance_km', models.FloatField()),
                ('destination_language', models.CharField(max_length=3)),
                ('language_levenshtein_distance', models.FloatField()),
            ],
        ),
    ]
