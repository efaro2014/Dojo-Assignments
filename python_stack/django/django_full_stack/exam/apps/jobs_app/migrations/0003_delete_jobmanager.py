# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-20 18:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0002_job_jobmanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JobManager',
        ),
    ]
