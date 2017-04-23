import random

from django.http import HttpResponse
from slackclient import SlackClient


class Irobot(object):
    """ slack bot using events api, refer https://api.slack.com/events-api """

    def __init__(self, **kwargs):
        """ initialize bot """
        token = kwargs.pop('token')
        self.client = SlackClient(token.access_token)

    def url_verification(self, event):
        """ event handler for url_verification, refer https://api.slack.com/events/url_verification """
        return HttpResponse(event.get('challenge'))

    def message(self, event):
        """ event handler for message.im, refer https://api.slack.com/events/message.im """
        reply = ''
        text = event.get('event').get('text')

        if 'i love you' in text:
            reply = 'I love you too dear :kiss:'

        elif 'its my birthday' in text:
            reply = 'Oh great!! Many many happy returns of the day dear :birthday: :tada:'

        elif 'tell me a joke' in text:
            jokes = [
                'Born free, taxed to death :smile:',
                'For Sale: Parachute. Only used once, never opened :smile:',
                'What is faster Hot or cold? Hot, because you can catch a cold :smile:',
            ]
            reply = random.choice(jokes)

        else:
            pass

        if reply:
            self.client.api_call(
                'chat.postMessage',
                channel=event.get('event').get('channel'),
                text=reply
            )

        return HttpResponse()
