# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 09:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0002_auto_20170319_0656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pending',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pending',
            name='sapip',
        ),
        migrations.AddField(
            model_name='pending',
            name='sapid',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='solution.Details'),
            preserve_default=False,
        ),
    ]
