# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 22:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='Документ')),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='docs')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название предмета')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Subject', verbose_name='Предмет'),
        ),
    ]
