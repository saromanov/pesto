from newspaper import Article

def get_articles_urls(url:str):
    if not url:
        raise Exception('url is not defined')
    papers = newspaper.build(url)
    for p in papers:
        yield p.url
