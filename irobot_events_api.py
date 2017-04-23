import os
import json

from flask import Flask
from flask import request

from slackclient import SlackClient


app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to irobot!'


@app.route('/events', methods=["POST"])
def events_endpoint():
    bot = Irobot()
    event = json.loads(request.data)
    event_type = event.get('type').replace('.', '_')
    event_handler = getattr(bot, event_type, False)
    if event_handler:
        return event_handler(event)
    return 'success'


class Irobot(object):
    """ slack bot using events api, refer https://api.slack.com/events-api """

    def __init__(self, **kwargs):
        """ initialize bot """
        self.client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
        self.client.rtm_connect()

    def url_verification(self, event):
        """event handler for url_verification, refer https://api.slack.com/events/url_verification """
        return event.get('challenge')

    def message_im(self, event):
        """ event handler for message.im, refer https://api.slack.com/events/message.im """
        self.client.api_call(
            'chat.postMessage',
            channel=event.get('channel'),
            text="Hello from Python! :tada:"
        )
