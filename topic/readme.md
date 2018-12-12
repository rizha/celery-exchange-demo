Topic exchange 
-------------------------
Topic exchanges route messages to queues based on wildcard matches between the routing key and something called the routing pattern specified by the queue binding.


Running Queue
-----------------
open termnial for each queueA & queueB folder and run

```
$ celery worker -A app -l info -n queueA@%h
$ celery worker -A app -l info -n queueB@%h
$ celery worker -A app -l info -n queueC@%h
```


Publish Message
---------------
run inside python intepreter and see result on termnial queueA, queueB and queueC
```
>>> from app import celery
>>> celery.send_task('app.process_agreements', exchange='agreements',routing_key='agreements.eu.headstore')
>>> celery.send_task('app.process_agreements', exchange='agreements', routing_key='agreements.eu')
>>> celery.send_task('app.process_agreements', exchange='agreements', routing_key='agreements.eu.berlin')
```