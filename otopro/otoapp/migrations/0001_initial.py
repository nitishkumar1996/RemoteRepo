# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-07-26 12:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cno', models.IntegerField()),
                ('cname', models.CharField(max_length=100)),
                ('cfee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('sname', models.CharField(max_length=100)),
                ('slocation', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='abc',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='otoapp.Student'),
        ),
    ]
