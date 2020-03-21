import logging

from flask import Flask, render_template
from backend.elastic import elastic
from backend.db import db

def make_app(config=None):
    app = Flask(__name__)
    configure(app)
    configure_celery_app(app)
    configure_all()
    app.run()

def configure(app:Flask):
     app.config.from_object("pesto.configs.default.DefaultConfig")
     config = get_config(app, config)
     app.config["CONFIG_PATH"] = config
     app_config_from_env(app, prefix="PESTO_")

     configure_logging(app)

     deprecation_level = app.config.get("DEPRECATION_LEVEL", "default")


def configure_celery_app(app, celery):
    """Configures the celery app."""
    app.config.update({"BROKER_URL": app.config["CELERY_BROKER_URL"]})
    celery.conf.update(app.config)

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

def configure_all():
    elastic.init()

if __name__ == '__main__':
    make_app()
