Topic exchange 
-------------------------
The fanout copies and routes a received message to all queues that are bound to it.


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
>>> celery.send_task('app.process_sport_news', exchange='sport_news', routing_key='sport_news')
```