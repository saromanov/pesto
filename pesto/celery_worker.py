from app import make_app, configure_background_tasks
from backend.celery import celery

app = make_app()
configure_background_tasks(app)
celery.worker_main(["skylines.worker", "--loglevel=INFO"])