from celery import Celery

import settings

celery = Celery()
celery.config_from_object(settings)


@celery.task
def process_agreements():
    return 'processing agreements in QueueC'
