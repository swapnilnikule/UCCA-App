# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-02 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uccaApp', '0012_auto_20190402_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layers_categories_restrictions',
            name='resriction_type',
            field=models.CharField(choices=[('REQUIRE_SIBLING', 'require sibling'), ('REQUIRE_CHILD', 'require child'), ('FORBID_SIBILIMG', 'forbid sibilimg'), ('FORBID_CHILD', 'forbid child'), ('FORBID_ANY_CHILD', 'forbid any child'), ('UNIQUE_UNDER_PARENT', 'unique under parent'), ('NOT_UNARY', 'Cannot be a single non-remote child of a parent')], max_length=256),
        ),
    ]
