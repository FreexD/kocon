# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tartak', '0006_wood_kind_forest_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pieces',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order_item',
            name='is_using_regular_price',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order_item',
            name='detail_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]