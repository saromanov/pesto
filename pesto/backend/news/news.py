from typing import List
from newspaper import Article, hot
import os,sys,inspect

# https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk
# https://www.dataquest.io/blog/tutorial-text-classification-in-python-using-spacy/
# https://medium.com/@datamonsters/text-preprocessing-in-python-steps-tools-and-examples-bf025f872908

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from nlp import Processing

def get_articles_urls(url:str):
    if not url:
        raise Exception('url is not defined')
    papers = newspaper.build(url)
    for p in papers:
        yield p.url

def hot_topics() -> List[str]:
    return hot()

def get_article(url:str):
    article = Article(url)
    article.download()
    article.parse()
    #print(article.text)
    p = Processing(article.text)
    p.do()