import datetime
from elasticsearch import Elasticsearch

def init(config):
    es = Elasticsearch(config['ELASTIC_ADDRESS'])
    es.index(index='article_text', id=1, body = {'text': 'simple', 'datetime': datetime.datetime.now()})

def remove_from_index(app, index, model):
    app.elasticsearch.delete(index=index, id=model.id)