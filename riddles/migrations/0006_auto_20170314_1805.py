# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0005_auto_20170314_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solution',
            old_name='sol_des',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='solution',
            old_name='sol_image',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='solution',
            name='riddle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riddles.Riddles'),
        ),
    ]
