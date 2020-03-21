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
from sqlalchemy.sql.expression import cast, case
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from source import Source

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(Integer, autoincrement=True, primary_key=True)
    email_address = db.column_property(
        db.Column(Unicode(255)), comparator_factory=LowerCaseComparator
    )
    first_name = db.Column(Unicode(255), nullable=False)
    last_name = db.Column(Unicode(255))
    _password = db.Column("password", Unicode(128), nullable=False)

    login_time = db.Column(DateTime)

    def __init__(self, *args, **kwargs):
        self.generate_tracking_key()
        super(User, self).__init__(*args, **kwargs)
    
    @staticmethod
    def by_email_address(email):
        return User.query(email_address=email).first()
    
    @hybrid_property
    def name(self):
        if not self.last_name:
            return self.first_name

        return self.first_name + u" " + self.last_name