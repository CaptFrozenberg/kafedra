# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160706_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Документ')),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='docs')),
            ],
        ),
    ]