# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-03 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awsapp', '0006_auto_20170903_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='credentials',
            name='secretkey',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
