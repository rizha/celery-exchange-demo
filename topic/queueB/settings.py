from kombu import Queue, Exchange


broker_url = 'amqp://guest:guest@localhost:5672//'

task_queues = (
    Queue('queueB', exchange=Exchange('agreements', type='topic'),
          routing_key='agreements.#'),
)

task_create_missing_queues = False
