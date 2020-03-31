from celery import Celery
from flask import Flask

def make_celery(self, app:Flask):
    self.name = app.import_name
    self.config_from_object(app.config)
    TaskBase = self.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    self.Task = ContextTask

celery = Celery(include=["pesto.backend.celery.tasks"])
Celery.init_app = make_celery

@celery.task
def store_hot_topics():
    print('YES')