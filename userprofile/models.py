#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from _ast import Lambda

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    country = models.CharField(max_length=150, verbose_name="Kraj")
    age = models.CharField(max_length=3, verbose_name="Wiek")
    
User.profile = property(Lambda u:UserProfile.objects.get_or_create(user=u)[0]) 