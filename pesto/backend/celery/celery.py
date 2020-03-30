import celery
from celery.task import periodic_task
from celery.schedules import crontab
from flask import Flask

def make_celery(app:Flask):
    celery_app = celery.Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    TaskBase = celery_app.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery_app.Task = ContextTask

celery = Celery(include=["pesto.backend.celery.tasks"])
celery.init_app = make_celery