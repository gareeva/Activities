# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='location',
            name='longtitude',
            field=models.CharField(max_length=10),
        ),
    ]
