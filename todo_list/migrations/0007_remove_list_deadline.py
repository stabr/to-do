# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-12 21:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0006_auto_20190112_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='deadline',
        ),
    ]
