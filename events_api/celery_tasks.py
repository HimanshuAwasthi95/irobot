import os

import celery
from handler import Irobot


app = celery.Celery('events_api_celery_tasks')
app.conf.update(
    BROKER_URL=os.environ['REDIS_URL'],
    CELERY_RESULT_BACKEND=os.environ['REDIS_URL']
)


@app.task
def process_event(data):
    event_type = data['type'].replace('.', '_')
    event_handler = getattr(Irobot, event_type, False)
    if event_handler:
        event_handler(data)
