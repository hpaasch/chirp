# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20160623_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos', verbose_name='Profile photo'),
        ),
    ]
