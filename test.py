#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os.path
import sys

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = 'b4d6009b38bc411eab958beb515722e6'


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'de'  # optional, default value equal 'en'

    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    request.query = "Hello"

    response = request.getresponse()
    result = json.loads(response.read())
    print result, type(result)
    # print (response.read())


if __name__ == '__main__':
    main()
