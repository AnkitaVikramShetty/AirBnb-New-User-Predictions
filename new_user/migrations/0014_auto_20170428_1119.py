# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0013_auto_20170428_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessions',
            name='secs_elapsed',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='sessions',
            name='user_id',
            field=models.CharField(max_length=50),
        ),
    ]
