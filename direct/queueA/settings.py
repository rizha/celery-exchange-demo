from kombu import Queue, Exchange

broker_url = 'amqp://guest:guest@localhost:5672//'

task_queues = (
    Queue('queueA', exchange=Exchange('pdf_events', type='direct'),
          routing_key='pdf_create'),
)

task_create_missing_queues = False