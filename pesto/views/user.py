from flask.view import MethodView
from flask import render_template, Blueprint, Flask
from model import User
from utils import register_view

class UserProfile(MethodView):
    def get(self, id):
        user = User.query.filter(id=id)
        return render_template('user.html', form=form, user=user)


def make_handlers(app:Flask):
    bp = Blueprint('user', __name__)
    register_view(bp, routes=['/users/profile'], view_func=UserProfile.as_view("user"))