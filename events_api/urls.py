# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^incoming/$', views.Incoming.as_view(), name='incoming'),
    url(r'^oauth/start/$', views.OauthStart.as_view(), name='oauth_start'),
    url(r'^oauth/finish/$', views.OauthFinish.as_view(), name='oauth_finish'),
]
