# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=10),
        ),
    ]
