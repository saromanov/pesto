import os

class Config:
    DEBUG = True
    ELASTIC_ADDRESS = 'http://localhost:9200'
    SECRET_KEY = os.urandom(32)