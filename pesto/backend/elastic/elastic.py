import datetime
import uuid

from elasticsearch7 import Elasticsearch

class Data:
    ''' saving of article to elastic search format
    '''
    def __init__(self, text):
        self.text = text
        self.datetime = datetime.datetime.now()
    
    def to_json(self):
        return {}
def init(config):
    es = Elasticsearch(config['ELASTIC_ADDRESS'])

def add_to_index(es, index, body:Data):
    es.index(index=index, id=uuid.uuid4(), body=body.to_json())

def remove_from_index(app, index, model):
    app.elasticsearch.delete(index=index, id=model.id)