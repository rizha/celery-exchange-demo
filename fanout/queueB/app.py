from celery import Celery

import settings

celery = Celery()
celery.config_from_object(settings)


@celery.task
def process_sport_news():
    return 'processing sport news in QueueB'

