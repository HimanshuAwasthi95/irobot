# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Tokens


class TokensAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tokens, TokensAdmin)
