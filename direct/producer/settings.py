from collections import namedtuple


broker_url = 'amqp://guest:guest@localhost:5672//'

task_create_missing_queues = False
task_routes = {
    'app.create_pdf': {
        'exchange': 'pdf_events',
        'routing_key': 'pdf_create'
    },
    'app.create_pdf_log': {
        'exchange': 'pdf_events',
        'routing_key': 'pdf_log'
    },
}
