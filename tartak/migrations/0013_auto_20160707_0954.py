# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 09:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tartak', '0012_auto_20160707_0941'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contractor',
            options={'verbose_name': 'Kontrahent', 'verbose_name_plural': 'Kontrahenci'},
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'verbose_name': 'Kierowca', 'verbose_name_plural': 'Kierowcy'},
        ),
        migrations.AlterModelOptions(
            name='forest_district',
            options={'verbose_name': 'Nadle\u015bnictwo', 'verbose_name_plural': 'Nadle\u015bnictwa'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Zam\xf3wienie', 'verbose_name_plural': 'Zam\xf3wienia'},
        ),
        migrations.AlterModelOptions(
            name='order_item',
            options={'verbose_name': 'Pozycja zam\xf3wienia', 'verbose_name_plural': 'Pozycje zam\xf3wienia'},
        ),
        migrations.AlterModelOptions(
            name='shipment',
            options={'verbose_name': 'Dostawa', 'verbose_name_plural': 'Dostawy'},
        ),
        migrations.AlterModelOptions(
            name='wood_kind',
            options={'verbose_name': 'Rodzaj drewna', 'verbose_name_plural': 'Rodzaje drewna'},
        ),
    ]