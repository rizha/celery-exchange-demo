from kombu.common import Broadcast

broker_url = 'amqp://guest:guest@localhost:5672//'

task_queues = (Broadcast('sport_news', routing_key='sport_news'),)

task_create_missing_queues = False