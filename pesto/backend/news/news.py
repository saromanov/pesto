from typing import List
from newspaper import Article, hot

def get_articles_urls(url:str):
    if not url:
        raise Exception('url is not defined')
    papers = newspaper.build(url)
    for p in papers:
        yield p.url

def hot_topics() -> List[str]:
    return hot()

article = Article('https://www.nytimes.com/2020/03/28/world/coronavirus-live-news-updates.html')
article.download()
article.parse()
article.nlp()
print(article.keywords)
print(article.summary)

print(hot_topics())
