import logging
import os
from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from backend.elastic import elastic
from backend.auth import login_manager
from backend.cache import client
from backend.celery import celery
from views import user, make_blueprints_user, make_blueprints_pesto, make_blueprints_sources
from config import Config, DevConfig, ProdConfig

logger = logging.getLogger(__name__)

def make_app(config=None):
    ''' create of the basic app without http handlers
    ''' 
    app = Flask(__name__)
    app.logger.info('Configuration of the app...')
    configure(app)
    app.logger.info('Configuration of backend...')
    configure_backend(app)
    return app

def make_http_app():
    app = make_app()
    app.logger.info('Configuration of handlers...')
    configure_handlers(app)
    app.logger.info('Configuration of blueprints...')
    configure_blueprints(app)
    app.logger.info('Configuration of background tasks...')
    configure_background_tasks(app)
    app.run()

def configure(app:Flask):
     config = get_config(app)
     app.config["CONFIG_PATH"] = config
     app_config_from_env(app, prefix="PESTO_")

     configure_logger(app)
     login_manager.init_app(app)

     deprecation_level = app.config.get("DEPRECATION_LEVEL", "default")


def configure_background_tasks(app:Flask):
    """Configures the celery app"""
    return celery.init_app(app)


def get_config(app:Flask):
    conf = os.getenv('PESTO_ENV', 'DEV')
    conf_name = 'config.config.DevConfig'
    if conf == 'PROD':
        conf_name = 'config.config.ProdConfig'
    app.config.from_object(conf_name)
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
    make_blueprints_sources(app)

def configure_backend(app:Flask):
    from backend.db import db
    db.init_app(app)
    db.app = app
    db.create_all()
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

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
    make_http_app()
