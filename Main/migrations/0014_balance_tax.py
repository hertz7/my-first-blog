# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-04 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0013_auto_20161004_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='tax',
            field=models.FloatField(null=True),
        ),
    ]
