# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0014_auto_20170428_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='age_gender_bkts',
            name='population_in_thousands',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='age_gender_bkts',
            name='year',
            field=models.FloatField(null=True),
        ),
    ]
