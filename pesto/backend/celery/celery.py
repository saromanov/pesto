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

celery = Celery(include=["backend.celery.tasks"], broker='redis://localhost:6379')
Celery.init_app = make_celery

@celery.task(bind=True)
def store_hot_topics():
    print('YES')
celery.add_periodic_task(1, store_hot_topics.s(), name='task-name')