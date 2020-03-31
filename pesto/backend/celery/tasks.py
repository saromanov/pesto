from .celery import celery 


@celery.task(bind=True)
def store_hot_topics(a):
    print('YESSSSSSS')