# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-02 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0002_auto_20200202_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('post', models.TextField()),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pics.Editor')),
            ],
        ),
    ]