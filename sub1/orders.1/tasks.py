from celery import shared_task

@shared_task
def get():
    return 'Process orders in sub1'


@shared_task
def update():
    return 'Update order in sub1'