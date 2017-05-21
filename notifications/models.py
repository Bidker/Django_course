#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import default
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
#import!!!!

class Notifications(models.Model):
  title = models.CharField(max_length = 150, verbose_name="Tytuł")  
  content = models.TextField(verbose_name = "Wiadomość")
  viewed = models.BooleanField(default=False, verbose_name="Otwarta")
  user = models.ForeignKey(User)
  
  def __unicode__(self):
      return self.title
  
@receiver(post_save, sender=User)
def send_welcome_message(sender, **kwargs):
    if kwargs.get('created', False):
        Notifications.objects.create(user=kwargs.get('instance'),
                                    title = "Witamy w serwisie",
                                    content = "To jest powitanie",
                                     )