# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tartak', '0008_auto_20160705_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_item',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
