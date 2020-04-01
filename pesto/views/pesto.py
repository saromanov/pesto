from flask.views import MethodView
from flask import render_template, Blueprint, Flask
from flask_login import login_required, current_user
from pluggy import HookimplMarker

from model import User
from utils import register_view
from forms import RegisterForm
from backend.auth import login_manager
from backend.cache import smembers
from backend.news import hot_topics
impl = HookimplMarker("pesto")

class Pesto(MethodView):
    
    @login_required
    def get(self):
        ''' 
        first, trying to get hot topics from cache
        if this is not available, then getting it from news scrapper
        '''
        topics = smembers('PESTO_SYSTEM_HOT_TOPICS')
        return render_template('main.html', topics=topics)
    
    def post(self):
        return render_template('main.html')

@impl(tryfirst=True)
def make_blueprints_pesto(app:Flask):
    '''
    Registering of user related blueprints
    '''
    bp = Blueprint('pesto', __name__)
    register_view(bp, routes=['/'], view_func=Pesto.as_view("pesto"))
    app.register_blueprint(bp)