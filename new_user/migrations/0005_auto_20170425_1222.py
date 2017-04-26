# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0004_auto_20170424_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_users',
            name='age',
            field=models.FloatField(null=True),
        ),
    ]
