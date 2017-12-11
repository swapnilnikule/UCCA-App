# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-11 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uccaApp', '0006_auto_20171211_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation_units',
            name='gui_status',
            field=models.CharField(choices=[('OPEN', 'Open'), ('HIDDEN', 'Hidden'), ('COLLAPSE', 'Collapse')], max_length=50),
        ),
        migrations.AlterField(
            model_name='layers',
            name='type',
            field=models.CharField(choices=[('ROOT', 'Root'), ('EXTENSION', 'Extension'), ('REFINEMENT', 'Refinement'), ('COARSENING', 'Coarsening')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='layers_categories_restrictions',
            name='resriction_type',
            field=models.CharField(choices=[('REQUIRE_SIBLING', 'require sibling'), ('REQUIRE_CHILD', 'require child'), ('FORBID_SIBILIMG', 'forbid sibilimg'), ('FORBID_CHILD', 'forbid child'), ('FORBID_ANY_CHILD', 'forbid any child')], max_length=256),
        ),
        migrations.AlterField(
            model_name='passages',
            name='type',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], max_length=50),
        ),
        migrations.AlterField(
            model_name='roles',
            name='name',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('PROJECT_MANAGER', 'Project Manager'), ('ANNOTATOR', 'Annotator'), ('GUEST', 'Guest')], max_length=50),
        ),
        migrations.AlterField(
            model_name='tabs',
            name='name',
            field=models.CharField(choices=[('USERS', 'Users'), ('PROJECTS', 'Projects'), ('TASKS', 'Tasks'), ('LAYERS', 'Layers'), ('PASSAGES', 'Passages'), ('SOURCES', 'Sources')], max_length=50),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('NOT_STARTED', 'NOT_STARTED'), ('ONGOING', 'ONGOING'), ('SUBMITTED', 'SUBMITTED'), ('REJECTED', 'REJECTED')], max_length=256),
        ),
    ]