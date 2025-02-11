# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-22 21:15
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lbst', '0029_auto_20171022_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='forest_agc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rast', django.contrib.gis.db.models.fields.RasterField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='forest_bgc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rast', django.contrib.gis.db.models.fields.RasterField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='gssurgo_soc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rast', django.contrib.gis.db.models.fields.RasterField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='landfire_classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('label', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='landfire_evt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rast', django.contrib.gis.db.models.fields.RasterField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='ndvi_2005',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rast', django.contrib.gis.db.models.fields.RasterField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='ndvi_2010',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rast', django.contrib.gis.db.models.fields.RasterField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='ndvi_2015',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rast', django.contrib.gis.db.models.fields.RasterField(srid=4326)),
            ],
        ),
    ]
