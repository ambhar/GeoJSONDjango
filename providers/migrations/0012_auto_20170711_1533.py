# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 15:33
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0011_auto_20170711_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='polygon',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326),
        ),
        migrations.AlterUniqueTogether(
            name='service',
            unique_together=set([('provider', 'polygon')]),
        ),
    ]