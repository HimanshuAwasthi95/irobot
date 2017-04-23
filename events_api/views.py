# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from urllib import urlencode

import requests
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View

from .handler import Irobot
from .models import Token


class Incoming(View):
    """ endpoint to handle the incoming messages from slack """

    def post(self, request, *args, **kwargs):
        """ POST method handler """

        # parse data
        incoming_data = json.loads(request.data)

        # invoke handler
        event_type = incoming_data['type'].replace('.', '_')
        event_handler = getattr(Irobot, event_type, False)
        if event_handler:
            return event_handler(incoming_data)

        # return 200 OK
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

    def get(self, request, *args, **kwargs):
        """ GET method handler """

        # prepare payload
        payload = {
            'code': request.GET['code'],
            'client_id': settings.SLACK['OAUTH']['CLIENT_ID'],
            'client_secret': settings.SLACK['OAUTH']['CLIENT_SECRET']
        }

        # prepare headers
        headers = {
            'content-type': 'application/json',
        }

        # prepare end point url
        end_point = "{}?{}".format(
            settings.SLACK['OAUTH']['ACCESS_END_POINT'],
            urlencode(payload)
        )

        # retrieve access token
        response = requests.post(end_point, json=payload, headers=headers)
        response.raise_for_status()
        response_data = response.json()

        # save data in db
        record = Token()
        record.team = response_data.get('team_id')
        record.auth_token_json = request.GET
        record.access_token_json = response_data
        record.save()

        # return 200 OK
        return HttpResponse('Oauth finished successfully')
