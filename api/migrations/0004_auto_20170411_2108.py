# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170326_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='next_due_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
