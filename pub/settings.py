from collections import namedtuple


broker_url = 'amqp://guest:guest@localhost:5672/event_dash'

task_create_missing_queues = False
task_routes = {
    'orders.tasks.*': {
        'exchange': 'orders',
        'routing_key': 'orders.*'
    },
    'stocks.tasks.*': {
        'exchange': 'stocks',
        'routing_key': 'stocks.#'
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