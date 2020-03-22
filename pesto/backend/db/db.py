from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def query(cls, **kw):
    q = db.session.query(cls)

    if kw:
        q = q.filter_by(**kw)

    return q

def get(cls, id):
    return cls.query().get(id)