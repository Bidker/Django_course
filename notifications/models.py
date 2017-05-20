#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import default

class Notifications(models.Model):
  title = models.CharField(max_length = 150, verbose_name="Tytuł")  
  content = models.TextField(verbose_name = "Wiadomość")
  viewed = models.BooleanField(default=False, verbose_name="Otwarta")
  user = models.ForeignKey(User)