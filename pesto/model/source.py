from sqlalchemy.types import Integer, String
from backend.db import db

class Source(db.Model):
    __tablename__ = "sources"

    id = db.Column(Integer, primary_key=True)
    url = db.Column(String)
    title = db.Column(String)
