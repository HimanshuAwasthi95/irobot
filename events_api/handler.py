import json
import apiai
import os

from django.http import HttpResponse
from slackclient import SlackClient


class Irobot(object):
    """ slack bot using events api, refer https://api.slack.com/events-api """

    def __init__(self, **kwargs):
        """ initialize bot """
        self.token = kwargs.pop('token')
        self.client = SlackClient(self.token.access_token)

    def url_verification(self, event):
        """ event handler for url_verification, refer https://api.slack.com/events/url_verification """
        return HttpResponse(event.get('challenge'))

    def message(self, event):
        """ event handler for message.im, refer https://api.slack.com/events/message.im """

        if event.get('event').get('username') != 'irobot':

            # get response from api.ai
            ai = apiai.ApiAI(os.environ['API_AI_CLIENT_ACCESS_TOKEN'])
            request = ai.text_request()
            request.session_id = self.token.team
            request.query = event.get('event').get('text')
            response = json.loads(request.getresponse().read())

            # reply response back to slack
            self.client.api_call(
                'chat.postMessage',
                channel=event.get('event').get('channel'),
                text=response['result']['fulfillment']['speech']
            )

        return HttpResponse()
