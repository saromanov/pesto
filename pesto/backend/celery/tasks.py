import datetime
from .celery import celery 
from backend.news import hot_topics
from backend.cache import sadd

@celery.task(bind=True)
def store_hot_topics(a):
    sadd(datetime.datetime.now().strftime('hot-topics:%Y:%m:%d:%H'), ','.join(hot_topics()))