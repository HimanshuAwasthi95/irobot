# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import requests
from uuid import uuid4
from urllib import urlencode

from django.views.generic import View
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

from .handler import Irobot


class Incoming(View):
    """ endpoint to handle the incoming messages from slack """

    def post(self, request, *args, **kwargs):

        # parse data
        incoming_data = json.loads(request.data)

        # invoke handler
        event_type = incoming_data.get('type').replace('.', '_')
        event_handler = getattr(Irobot, event_type)
        event_handler(incoming_data)
        return HttpResponse()


class OauthStart(View):
    """ endpoint to initiate the oauth process """

    def get(self, request, *args, **kwargs):
        """ GET method handler """

        # prepare payload
        payload = {
            'client_id': settings.SLACK['OAUTH']['CLIENT_ID'],
            'scope': settings.SLACK['OAUTH']['SCOPES'],
        }

        # prepare end point url
        end_point = "{}?{}".format(
            settings.SLACK['OAUTH']['AUTH_END_POINT'],
            urlencode(payload)
        )

        # redirect to end point url
        return HttpResponseRedirect(end_point)


class OauthFinish(View):
    """ endpoint to which the slack will post the authorization code """

    def post(self, request, *args, **kwargs):
        """ POST method handler """

        # parse data
        incoming_data = json.loads(request.data)

        # prepare payload
        payload = {
            'code': incoming_data.get('code'),
            'client_id': settings.SLACK['OAUTH']['CLIENT_ID'],
            'client_secret': settings.SLACK['OAUTH']['CLIENT_SECRET']
        }

        # prepare end point url
        end_point = "{}?{}".format(
            settings.SLACK['OAUTH']['ACCESS_END_POINT'],
            urlencode(payload)
        )

        # retrieve access token
        response = requests.post(end_point, json=payload)
        response.raise_for_status()

        # parse data
        response_data = response.json()
        access_token = response_data.get('access_token')

        return HttpResponse()
