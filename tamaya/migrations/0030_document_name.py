# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-13 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamaya', '0029_buffered_bndry'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(default='filename', max_length=40),
            preserve_default=False,
        ),
    ]
