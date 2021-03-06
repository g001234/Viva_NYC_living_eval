# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-04 22:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('geolocation_app', '0002_googleresult_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='googleresult_time',
            name='r_address',
        ),
        migrations.RemoveField(
            model_name='googleresult_time',
            name='r_address2',
        ),
        migrations.AddField(
            model_name='googleresult_time',
            name='r_destlat',
            field=models.FloatField(default=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='googleresult_time',
            name='r_destlon',
            field=models.FloatField(default=-73),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='googleresult_time',
            name='r_startlat',
            field=models.FloatField(default=41),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='googleresult_time',
            name='r_startlon',
            field=models.FloatField(default=-72),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='googleresult_time',
            name='r_time',
            field=models.CharField(max_length=20),
        ),
    ]
