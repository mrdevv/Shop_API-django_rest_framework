# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20171208_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='quantity',
            field=models.SmallIntegerField(default=0),
        ),
    ]
