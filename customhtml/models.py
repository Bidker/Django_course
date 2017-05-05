#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class CustomHtml(models.Model):
    title = models.CharField(max_length=150, verbose_name="Tytuł")
    sourcehtml = models.TextField(verbose_name="Kod html")
    
    def __unicode__(self):
        return self.title