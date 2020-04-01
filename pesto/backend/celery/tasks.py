import datetime
from .celery import celery 
from backend.news import hot_topics
from backend.cache import sadd
from backend.utils import time_now_formatted

@celery.task(bind=True)
def store_hot_topics(a):
    sadd(time_now_formatted('PESTO_SYSTEM_HOT_TOPICS'), hot_topics())