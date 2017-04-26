# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0008_results'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='country_destination',
            field=models.CharField(max_length=50),
        ),
    ]
