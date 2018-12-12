from celery import shared_task

@shared_task
def get():
    return 'Process stocks in sub1'


@shared_task
def update():
    return 'Update stocks in sub1'