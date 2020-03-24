from datetime import datetime
from hashlib import sha256

from sqlalchemy.types import (
    Unicode,
    Integer,
    BigInteger,
    SmallInteger,
    DateTime,
    Boolean,
    Interval,
    String,
)
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql.expression import cast, case
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from backend.db import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(Integer, primary_key=True)
    email = db.column_property(
        db.Column(Unicode(255))
    )
    first_name = db.Column(Unicode(255), nullable=False)
    last_name = db.Column(Unicode(255))
    password = db.Column("password", Unicode(128), nullable=False)

    login_time = db.Column(DateTime)

    def __init__(self, *args, **kwargs):
        kwargs['password'] = generate_password_hash(kwargs.get('password'))
        super(User, self).__init__(*args, **kwargs)
    
    @staticmethod
    def by_email(email):
        return User.query.filter_by(email=email).first()
    
    @hybrid_property
    def name(self):
        if not self.last_name:
            return self.first_name

        return self.first_name + u" " + self.last_name