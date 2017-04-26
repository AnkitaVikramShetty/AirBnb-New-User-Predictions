# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0007_pre_processed_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='results',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('results_id', models.CharField(max_length=50)),
                ('country_destination', models.ForeignKey(to='new_user.countries')),
            ],
        ),
    ]
