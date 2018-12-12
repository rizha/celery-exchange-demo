from kombu import Queue, Exchange
from kombu.common import Broadcast
broker_url = 'amqp://guest:guest@localhost:5672//'

task_queues = (
    Queue('queueB', exchange=Exchange('pdf_events', type='direct'),
          routing_key='pdf_log'),
)

task_create_missing_queues = False
