from flask.views import MethodView
from flask import render_template, Blueprint, Flask, request
from flask_login import login_required, current_user
from pluggy import HookimplMarker

from model import Source
from utils import register_view
from forms import AddSourceForm
from backend.auth import login_manager
from backend.db import query, db
impl = HookimplMarker("pesto")

class AddSource(MethodView):
    ''' Add new source
    ''' 
    @login_required
    def get(self):
        return render_template('add_source.html', form=AddSourceForm())
    
    @login_required
    def post(self):
        form = AddSourceForm(request.form)
        if not form.validate_on_submit():
            self.redirect_failed()
            return
        source = Source(url=form.source.data, title=form.title.data, user_id=current_user.id)
        db.session.add(source)
        db.session.commit()
        return render_template('add_source.html', form=form)
    
    def redirect_failed(self):
        flash('Unable to add new source')
        return self.get()
        
class ShowSource(MethodView):
    ''' Showing of registerd sources for user
    '''
    @login_required
    def get(self):
        return render_template('sources.html', sources=Source.query.filter_by(user_id=current_user.id))

@impl(tryfirst=True)
def make_blueprints_sources(app:Flask):
    '''
    Registering of user related blueprints
    '''
    bp = Blueprint('source', __name__)
    register_view(bp, routes=['/sources/add'], view_func=AddSource.as_view("source"))
    register_view(bp, routes=['/sources'], view_func=ShowSource.as_view("source_show"))
    app.register_blueprint(bp)