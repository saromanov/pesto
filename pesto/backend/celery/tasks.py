from .celery import celery

@celery.task
def store_hot_topics():
    print('YES')