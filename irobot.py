import os
import time

from slackclient import SlackClient


class Irobot(object):
    """ slack bot """

    def __init__(self, **kwargs):
        """ initialize bot """
        self.client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

    def connect(self):
        """ read messages and dispatch to handler """
        while True:
            for event in self.client.rtm_read():
                event_type = event.get('type').replace('.', '_')
                event_handler = getattr(self, event_type)
                if event_handler:
                    event_handler(event)
                time.sleep(1)

    def hello(self, message):
        """ event handler for hello, refer https://api.slack.com/rtm#events for more events """
        pass

    def message_im(self, message):
        """ event handler for message.im """
        self.client.api_call(
            'chat.postMessage',
            channel=message.get('channel'),
            text='I love some one direct messaging me :tada:'
        )


if __name__ == '__main__':
    bot = Irobot()
    bot.connect()
