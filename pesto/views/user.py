from flask.views import MethodView
from flask import render_template, Blueprint, Flask
from pluggy import HookimplMarker

from model import User
from utils import register_view

impl = HookimplMarker("pesto")

class UserProfile(MethodView):
    def get(self, id):
        user = User.query.filter(id=id)
        return render_template('user.html', form=form, user=user)

@impl(tryfirst=True)
def make_blueprints(app:Flask):
    '''
    Registering of user related blueprints
    '''
    bp = Blueprint('user', __name__)
    register_view(bp, routes=['/users/profile'], view_func=UserProfile.as_view("user"))
    app.register_blueprint(bp)
    print('resss')