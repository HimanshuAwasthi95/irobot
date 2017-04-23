# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Token


class TokensAdmin(admin.ModelAdmin):
    name = 'events_api'
    verbose_name = 'Events API'


admin.site.register(Token, TokensAdmin)
