# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20161013_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='rating',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
