# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-07 19:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('geolocation_app', '0003_auto_20151204_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleResult_steps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='googleresult_time',
            name='destination2',
            field=models.CharField(default=datetime.datetime(2017, 4, 7, 19, 25, 52, 356846, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='googleresult_time',
            name='origin',
            field=models.CharField(default=datetime.datetime(2017, 4, 7, 19, 26, 3, 932067, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
