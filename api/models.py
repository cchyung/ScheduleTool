# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Class(models.Model):
    type = models.CharField(max_length=5, default='DFLT')
    dept = models.CharField(max_length=5, 'NONE')
    code = models.IntegerField()
    suffix = models.CharField(max_length=4, blank=True)
    section = models.CharField(max_length=6, default='000000')
    days = models.CharField(max_length=10, default='XXX')
    begin = models.IntegerField()
    end = models.IntegerField()

class CoreqClass(Class):
    models.ForeignKey(Class, on_delete=models.CASCADE)
