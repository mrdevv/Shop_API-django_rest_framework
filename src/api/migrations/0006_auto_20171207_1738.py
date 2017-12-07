# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 17:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_orderproducts_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproducts',
            name='order_uuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderproducts', to='api.Order'),
        ),
    ]
