# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-07-26 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otoapp', '0004_auto_20190726_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='abc',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='otoapp.Student'),
        ),
    ]
