# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='truckType',
            field=models.CharField(default='Грузовик1', max_length=35),
        ),
    ]
