# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StopWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=26)),
            ],
        ),
        migrations.AlterModelOptions(
            name='chirp',
            options={'ordering': ['-created']},
        ),
    ]
