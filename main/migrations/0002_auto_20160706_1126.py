# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurs',
            name='number',
            field=models.IntegerField(unique=True, verbose_name='Курс'),
        ),
    ]
