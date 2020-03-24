from flask.views import MethodView
from flask import render_template, Blueprint, Flask, redirect, flash, request
from pluggy import HookimplMarker
from flask_login import UserMixin

from model import User
from utils import register_view
from forms import RegisterForm
from backend.db import db

impl = HookimplMarker("pesto")

class UserProfile(MethodView):
    def get(self, id):
        return render_template('user.html', form=form, user=user)

class UserLogin(UserMixin, MethodView):
    def post(self):
        form = LoginForm()

class UserRegister(MethodView):
    def get(self):
        return self.render(RegisterForm())
    
    def post(self):
        form = RegisterForm(request.form)
        if form.validate_on_submit():
            email = form.email.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            password = form.password.data
            if User.by_email(email):
                flash('User ealready exisr')
                return redirect('/')
            user = User(email=email, first_name=first_name, last_name=last_name, password=password)
            db.session.add(user)
            db.session.commit()
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
    register_view(bp, routes=['/users/login'], view_func=UserLogin.as_view("login"))
    register_view(bp, routes=['/users/register'], view_func=UserRegister.as_view("register"))
    app.register_blueprint(bp)