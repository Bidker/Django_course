# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-05 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.FileField(default=None, upload_to='media/images/', verbose_name='Obraz'),
            preserve_default=False,
        ),
    ]
