Topic exchange 
-------------------------
Delivers messages to queues based on a message routing key.


Running Queue
-----------------
open termnial for each queueA & queueB folder and run

```
$ celery worker -A app -l info -n queueA@%h
$ celery worker -A app -l info -n queueB@%h
```


Publish Message
---------------
run inside python intepreter and see result on termnial queueA and queueB
```
>>> from app import celery
>>> celery.send_task('app.create_pdf')
>>> celery.send_task('app.create_pdf_log')
```