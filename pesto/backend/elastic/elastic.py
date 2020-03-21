from elasticsearch import Elasticsearch

def init(config):
    es = Elasticsearch(config['ELASTIC_ADDRESS'])
    es.add_index(index='article_text', id=1)

def remove_from_index(app, index, model):
    app.elasticsearch.delete(index=index, id=model.id)