# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-10-28 15:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcbc', '0002_auto_20191028_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frog_bay_trails',
            name='layer',
        ),
        migrations.RemoveField(
            model_name='frog_bay_trails',
            name='path',
        ),
        migrations.RemoveField(
            model_name='frog_bay_trails',
            name='shape_len',
        ),
        migrations.RemoveField(
            model_name='frog_bay_trails',
            name='tiger_feat',
        ),
    ]
