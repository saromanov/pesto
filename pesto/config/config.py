import os

class Config:
    DEBUG = False
    ELASTIC_ADDRESS = 'http://localhost:9200'
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False