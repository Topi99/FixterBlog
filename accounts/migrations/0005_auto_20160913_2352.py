# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160803_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tel',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]