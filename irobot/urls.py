# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include


urlpatterns = [
    url(r'^events-api/', include('events_api.urls')),
]
