from flask.views import MethodView
from flask import render_template, Blueprint, Flask
from flask_login import login_required, current_user
from pluggy import HookimplMarker

from model import User
from utils import register_view
from forms import RegisterForm
from backend.auth import login_manager

impl = HookimplMarker("pesto")

class Pesto(MethodView):
    decoratorss = [login_manager.user_loader]
    
    @login_required
    def get(self):
        return render_template('main.html')
    
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