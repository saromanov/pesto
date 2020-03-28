import os

class Config:
    DEBUG = False
    ELASTIC_ADDRESS = 'http://localhost:9200'
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    POSTGRES_USER = 'pesto'
    POSTGRES_URL = '127.0.0.1:5432'
    POSTGRES_DB = 'pesto'
    POSTGRES_PASSWORD = 'pesto'
    SQLALCHEMY_DATABASE_URI = DB_URL = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_URL}/{POSTGRES_DB}'
    CELERY_BROKER_URL='redis://localhost:6379'
    CELERY_RESULT_BACKEND='redis://localhost:6379'

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False