# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-03 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0008_auto_20161003_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='flag',
            field=models.IntegerField(default=0),
        ),
    ]
