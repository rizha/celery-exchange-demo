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


# Order tasks
Order = namedtuple('Order', ['get', 'update'])
Order.get = 'orders.tasks.get'
Order.update = 'orders.tasks.update'


# Stock.tasks
Stock = namedtuple('Stock', ['get', 'update'])
Stock.get = 'stocks.tasks.get'
Stock.update = 'stocks.tasks.update'