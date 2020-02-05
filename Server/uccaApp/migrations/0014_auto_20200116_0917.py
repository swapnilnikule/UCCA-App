# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2020-01-16 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uccaApp', '0013_auto_20190402_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation_units',
            name='comment',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='logaction',
            name='comment',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='loglogin',
            name='comment',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='loglogin',
            name='data',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='manager_comment',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='user_comment',
            field=models.CharField(blank=True, default='', max_length=10000),
        ),
    ]