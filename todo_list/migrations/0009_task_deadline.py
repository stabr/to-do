# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-13 09:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0008_auto_20190113_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
