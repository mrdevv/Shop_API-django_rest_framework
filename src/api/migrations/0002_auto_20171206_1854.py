# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerprofile',
            old_name='id',
            new_name='uuid',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer_id',
            new_name='customer_uuid',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_id',
            new_name='order_uuid',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product_id',
            new_name='product_uuid',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='shop_id',
            new_name='shop_uuid',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_id',
            new_name='product_uuid',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='shop_id',
            new_name='shop_uuid',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='id',
        ),
        migrations.AddField(
            model_name='stock',
            name='stock_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
