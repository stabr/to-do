# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-12 19:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_auto_20190112_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]