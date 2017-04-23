import os

from django.http import HttpResponse
from slackclient import SlackClient


class Irobot(object):
    """ slack bot using events api, refer https://api.slack.com/events-api """

    def __init__(self, **kwargs):
        """ initialize bot """
        self.client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
        self.client.rtm_connect()

    def url_verification(self, event):
        """event handler for url_verification, refer https://api.slack.com/events/url_verification """
        return HttpResponse(event.get('challenge'))

    def message(self, event):
        """ event handler for message.im, refer https://api.slack.com/events/message.im """
        if event.get('event').get('bot_id') != os.environ.get('SLACK_BOT_ID'):
            self.client.api_call(
                'chat.postMessage',
                user='irobot',
                as_user=True,
                channel=event.get('event').get('channel'),
                text="Hello from Python! :tada:"
            )
        return HttpResponse()
