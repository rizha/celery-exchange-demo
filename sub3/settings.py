from kombu import Queue, Exchange
from kombu.common import Broadcast
broker_url = 'amqp://guest:guest@localhost:5672/event_dash'

task_queues = (
    Queue('sub3', exchange=Exchange('stocks', type='topic'), routing_key='stocks.#'),
)

task_create_missing_queues = False
