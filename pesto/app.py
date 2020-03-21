import logging

from flask import Flask, render_template


def make_app(config=None):
    app = Flask(__name__)

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

logger = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main_page():
    return render_template('main.html')

@app.route('/sources', methods=['GET'])
def main_page():
    return render_template('source.html')

if __name__ == '__main__':
    app.run()
