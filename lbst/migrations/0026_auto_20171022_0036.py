# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-22 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lbst', '0025_auto_20171022_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='c_avoided_conversion',
            name='avoided_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='c_avoided_conversion',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
