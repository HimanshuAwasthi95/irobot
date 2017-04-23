# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.models import User


def create_users(apps, schema_editor):
    if not schema_editor.connection.alias == 'default':
        return
    User(
        username='akhilputhiry',
        email='akhilputhiry@gmail.com',
        first_name='Akhil',
        last_name='Lawrence',
        is_staff=True,
        is_active=True,
        is_superuser=True
    ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('events_api', "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_users),
    ]
