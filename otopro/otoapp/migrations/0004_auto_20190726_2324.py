# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-07-26 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otoapp', '0003_auto_20190726_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='abc',
            field=models.OneToOneField(null=True, on_delete=models.SET(3), to='otoapp.Student'),
        ),
    ]
