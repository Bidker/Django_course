# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-05 07:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
    ]
