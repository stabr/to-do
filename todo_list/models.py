# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# from django.utils.timezone import now
from datetime import datetime

# Create your models here.


class Task(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateField(default=datetime.now, blank=True)
    asignee = models.CharField(default='John', max_length=200)

    def __str__(self):
        return self.item + ' | ' + str(self.completed) + ' | ' + str(self.id)
