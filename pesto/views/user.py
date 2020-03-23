from flask.views import MethodView
from flask import render_template, Blueprint, Flask, redirect
from pluggy import HookimplMarker

from model import User
from utils import register_view
from forms import RegisterForm

impl = HookimplMarker("pesto")

class UserProfile(MethodView):
    def get(self, id):
        return render_template('user.html', form=form, user=user)

class UserRegister(MethodView):
    def get(self):
        return self.render(RegisterForm())
    
    def post(self):
        form = RegisterForm()
        if form.validate_on_submit():
            return redirect('/')
        return "Error"
    
    def render(self, form):
        return render_template('register.html', form=form)

@impl(tryfirst=True)
def make_blueprints_user(app:Flask):
    '''
    Registering of user related blueprints
    '''
    bp = Blueprint('user', __name__)
    register_view(bp, routes=['/users/profile'], view_func=UserProfile.as_view("user"))
    register_view(bp, routes=['/users/register'], view_func=UserRegister.as_view("register"))
    app.register_blueprint(bp)