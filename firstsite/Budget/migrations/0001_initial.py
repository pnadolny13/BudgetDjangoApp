# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 00:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files_type', models.CharField(max_length=20)),
                ('input_title', models.CharField(max_length=200)),
                ('is_favorite', models.BooleanField(default=False)),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Budget.Expense')),
            ],
        ),
    ]
