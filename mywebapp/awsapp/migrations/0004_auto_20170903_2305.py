# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-03 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awsapp', '0003_credentials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='accesskey',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='accountid',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='secretkey',
            field=models.CharField(max_length=100),
        ),
    ]
