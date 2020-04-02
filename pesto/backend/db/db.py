from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def query(cls, **kw):
    q = db.session.query(cls)

    if kw:
        q = q.filter_by(**kw)

    return q

def get_by_id(cls, id):
    return db.session.query(cls).get(id)