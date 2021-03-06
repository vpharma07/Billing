# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-01-11 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_auto_20190111_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoices',
            name='Exp_Date',
            field=models.DateField(default=None, verbose_name='Expiry Date'),
        ),
        migrations.AddField(
            model_name='invoices',
            name='Price',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='invoices',
            name='p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.Products'),
        ),
    ]
