from flask.views import MethodView
from flask import render_template, Blueprint, Flask, redirect, flash, request, url_for
from pluggy import HookimplMarker
from flask_login import UserMixin, login_required, login_user

from model import User
from utils import register_view
from forms import RegisterForm, LoginForm
from backend.db import db, get_by_id
from backend.auth import login_manager

impl = HookimplMarker("pesto")

class UserProfile(MethodView):
    def get(self, id):
        return render_template('user.html', form=form, user=user)

class UserLogin(UserMixin, MethodView):
    def get(self):
        return render_template('login.html', form=LoginForm())
    
    def redirect_failed(self):
        flash('Invalid login or password')
        return self.get()

    def post(self):
        form = LoginForm(request.form)
        if not form.validate_on_submit():
            return self.redirect_failed()
        user = User.by_email(email=form.email.data)
        if not user:
            return self.redirect_failed()
        if not user.check_password(form.password.data):
            return self.redirect_failed()
        login_user(user)
        next = request.args.get('next')
        return redirect(next or url_for('pesto.pesto'))

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
                flash('User already exist')
                return self.get()
            user = User(email=email, first_name=first_name, last_name=last_name, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        return "Error"
    
    def render(self, form):
        return render_template('register.html', form=form)

@login_manager.user_loader
def user_loader(id):
    return get_by_id(User, id)

@impl(tryfirst=True)
def make_blueprints_user(app:Flask):
    '''
    Registering of user related blueprints
    '''
    bp = Blueprint('user', __name__)
    register_view(bp, routes=['/users/profile'], view_func=UserProfile.as_view("user"))
    register_view(bp, routes=['/login'], view_func=UserLogin.as_view("login"))
    register_view(bp, routes=['/register'], view_func=UserRegister.as_view("register"))
    app.register_blueprint(bp)