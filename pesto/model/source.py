from sqlalchemy.types import Integer, String

class Source(db.Model):
    __tablename__ = "sources"

    id = db.Column(Integer, autoincrement=True, primary_key=True)
    url = db.Column(String, autoincrement=True, primary_key=True)
