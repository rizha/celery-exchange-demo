from celery import Celery

import settings

celery = Celery()
celery.config_from_object(settings)


@celery.task
def create_pdf_log():
    return 'log has been create in queueB'
