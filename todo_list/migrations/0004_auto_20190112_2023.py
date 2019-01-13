# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-12 20:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_auto_20190112_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('asignee', models.CharField(default='John', max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]