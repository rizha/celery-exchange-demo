from kombu import Queue, Exchange
from kombu.common import Broadcast
broker_url = 'amqp://guest:guest@localhost:5672//'

task_queues = (
    Queue('queueA', exchange=Exchange('agreements', type='topic'),
          routing_key='agreements.eu.berlin.#'),
)

task_create_missing_queues = False