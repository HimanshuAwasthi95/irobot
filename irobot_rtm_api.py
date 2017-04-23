import os
import sys
import time
import logging

from slackclient import SlackClient


log_handler = logging.StreamHandler(sys.stdout)
log_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
log_handler.setLevel(logging.DEBUG)
log = logging.getLogger(__name__)
log.addHandler(log_handler)


class Irobot(object):
    """ slack bot using rtm api, refer https://api.slack.com/rtm """

    def __init__(self, **kwargs):
        """ initialize bot """
        self.client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
        self.client.rtm_connect()

    def run(self):
        """ read messages and dispatch to handler """
        while True:
            for event in self.client.rtm_read():
                log.debug(event)
                event_type = event.get('type').replace('.', '_')
                event_handler = getattr(self, event_type, False)
                if event_handler:
                    event_handler(event)
                time.sleep(1)

    def hello(self, event):
        """ event handler for hello, refer https://api.slack.com/rtm#events for more events """
        pass

    def message(self, event):
        """ event handler for message, refer https://api.slack.com/events/message """
        if event.get('username') != 'mybot':
            self.client.api_call(
                'chat.postMessage',
                user='mybot',
                as_user=True,
                channel=event.get('channel'),
                text="Hello from Python! :tada:"
            )


if __name__ == '__main__':
    bot = Irobot()
    bot.run()
