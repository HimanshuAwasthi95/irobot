# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import Incoming


urlpatterns = [
    url(r'^incoming/', Incoming.as_view(), name='incoming'),
]
