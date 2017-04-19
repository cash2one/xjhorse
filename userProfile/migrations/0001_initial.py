# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 04:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('localeCode', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('languageName', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, unique=True)),
                ('userName', models.CharField(blank=True, max_length=30)),
                ('mobile', models.CharField(max_length=15)),
                ('mobileVerified', models.BooleanField(default=False)),
                ('address', models.TextField(max_length=200)),
                ('localeCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userProfile.Languages')),
            ],
        ),
    ]
