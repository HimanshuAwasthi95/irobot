# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 14:00
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('team', models.CharField(max_length=100)),
                ('auth_token_json', django.contrib.postgres.fields.jsonb.JSONField()),
                ('access_token_json', django.contrib.postgres.fields.jsonb.JSONField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
