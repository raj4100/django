# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-02 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='mobile',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
