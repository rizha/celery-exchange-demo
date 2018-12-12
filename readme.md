Celery example exchange 
-------------------------
example of exchange in celery how it's look like, each of branch have their example:
- master(`topic`)
- direct(`direct`)
- fannout(`fanout`)

Requirements
-----------
- rabbitmq==3
- celery==4.2.0
- python==3.6


Configuration
-------------
make sure you create virtual_host: event_dash or anything you want but make sure to point all queue to that rabbitmq vhost.

Subscribe Message
-----------------
bellow are to run worker on each Queue Worker inside folder sub{n} change {n} to number 

```
$ celery worker -A app -l info -n sub{n}@%h
```


Publish Message
---------------
run inside python intepreter
```
>>> from settings import Order, Stock
>>> from app import celery
>>> celery.send_task(Order.get)
>>> celery.send_task(Stock.get)
```