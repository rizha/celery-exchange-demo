from celery import Celery

import settings

celery = Celery()
celery.config_from_object(settings)


@celery.task
def create_pdf():
    return 'pdf has been create in queueA'
