# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-06 11:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tamaya', '0011_ndvi_2010_ndvi_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forest_agc',
            old_name='raster',
            new_name='rast',
        ),
    ]
