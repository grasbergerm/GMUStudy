# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-09 23:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='group',
            name='time',
            field=models.TimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
