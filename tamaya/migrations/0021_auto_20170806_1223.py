# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-06 12:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tamaya', '0020_auto_20170806_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forest_bgc',
            old_name='raster',
            new_name='rast',
        ),
        migrations.RenameField(
            model_name='gssurgo_soc',
            old_name='raster',
            new_name='rast',
        ),
    ]
