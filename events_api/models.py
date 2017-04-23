# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from uuid import uuid4

from django.contrib.postgres import fields
from django.db import models


class Token(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    team = models.CharField(max_length=100)
    auth_token_json = fields.JSONField()
    access_token_json = fields.JSONField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified_on = models.DateTimeField(auto_now=True)
