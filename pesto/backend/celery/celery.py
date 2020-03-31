from celery import Celery
from flask import Flask

def make_celery(self, app:Flask):
    self.name = app.import_name
    self.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'backend.celery.tasks.store_hot_topics',
        'schedule': 1.0,
        },
    }
    self.conf.broker_url = app.config['CELERY_BROKER_URL']
    self.conf.result_backend = app.config['CELERY_RESULT_BACKEND']
    self.conf.timezone = 'UTC'
    TaskBase = self.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    self.Task = ContextTask

celery = Celery(include=["backend.celery.tasks"])
Celery.init_app = make_celery