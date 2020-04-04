from sqlalchemy import ForeignKey
from sqlalchemy.types import Integer, String
from backend.db import db

class Source(db.Model):
    __tablename__ = "sources"

    id = db.Column(Integer, primary_key=True)
    url = db.Column(String, nullable=False)
    title = db.Column(String, nullable=False)
    user_id = db.Column(Integer, ForeignKey('users.id'))