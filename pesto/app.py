import logging
import os

from flask import Flask, render_template
from backend.elastic import elastic
from views import user, make_blueprints_user, make_blueprints_pesto
from config import Config

import logging
logger = logging.getLogger(__name__)

def make_app(config=None):
    app = Flask(__name__)
    configure(app)
    configure_backend(app)
    configure_handlers(app)
    configure_blueprints(app)
    app.run()

def configure(app:Flask):
     app.config.from_object("config.config.Config")
     config = get_config(app)
     app.config["CONFIG_PATH"] = config
     app_config_from_env(app, prefix="PESTO_")

     configure_logger(app)

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

def get_config(app:Flask):
    project_dir = os.path.dirname(
        os.path.dirname(os.path.dirname(__file__))
    )
    project_config = os.path.join(project_dir, "pesto.cfg")
    instance_config = os.path.join(app.instance_path, "pesto.cfg")
    if os.path.exists(instance_config):
        return instance_config

def app_config_from_env(app:Flask, *args, **kwargs):
    '''
    getting convig variables from enviroment variables
    with special defined prefix.
    By default is PRESTO_
    '''
    prefix = kwargs.get('prefix')
    if not prefix:
        return
    for key in os.environ:
        if key.startswith(prefix):
            value = os.environ[key]
            if not value:
                continue
            app.config[key] = value

def configure_logger(app:Flask):
    '''
    provides configuration of the logger
    '''
    logger.setLevel(logging.INFO)
    if app.config.get("LOG_CONF_FILE"):
        logger.config.fileConfig(
            app.config["LOG_CONF_FILE"], disable_existing_loggers=False
        )

def configure_blueprints(app:Flask):
    make_blueprints_user(app)
    make_blueprints_pesto(app)

def make_config(config_path=None):
    if config_path is None:
        return Config()

def configure_backend(app:Flask):
    from backend.db import db
    db.init_app(app)
    db.app = app
    db.create_all()
    elastic.init(app.config)


def configure_handlers(app:Flask):
    configure_error_handlers(app)

def configure_error_handlers(app:Flask):

    @app.errorhandler(403)
    def page_403(sym):
        return render_template("forbidden_page.html"), 403
    
    @app.errorhandler(404)
    def page_404(sym):
        return render_template("not_found_page.html"), 404

if __name__ == '__main__':
    make_app()
