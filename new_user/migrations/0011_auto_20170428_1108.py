# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0010_train_users_2_signup_flow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train_users_2',
            name='country_destination',
            field=models.CharField(max_length=15),
        ),
    ]
