import celery
from flask import Flask

def make_celery(app:Flask):
    celery_app = celery.Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery_app.conf.beat_schedule = {
    "see-you-in-ten-seconds-task": {
        "task": "celery.store_hot_topics",
        "schedule": 1.0
        }
    }
    TaskBase = celery_app.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    @celery_app.task
    def store_hot_topics():
        print('YES')
    celery_app.Task = ContextTask
    celery_app.worker_main(['', '-B'])
    return celery_app


def store_hot_topics(celery):
    '''
    adding task for store hot topics
    '''
    pass