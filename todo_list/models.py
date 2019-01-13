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
    deadline = models.DateField(default=datetime.today, blank=True, null=True)
    # deadline = models.CharField(max_length=50)
    asignee = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.item + ' | ' + str(self.completed) + ' | ' + str(self.id)
