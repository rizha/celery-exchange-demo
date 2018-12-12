from celery import shared_task

@shared_task
def get():
    return 'Process orders in sub2'


@shared_task
def update():
    return 'update order in sub2'