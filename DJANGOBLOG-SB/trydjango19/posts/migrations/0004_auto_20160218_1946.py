# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-18 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20160216_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
