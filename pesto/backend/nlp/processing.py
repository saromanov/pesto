from typing import List
import string
from nltk import pos_tag, ne_chunk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import spacy
from spacy.lang.en import English

class Processing:
    def __init__(self, text:str):
        self._text = text
    
    def do(self):
        processed = basic_processing(self._text)
        tokenized = word_tokenize(self._text)
        methods = [remove_stopwords, stemming, ner]
        self._entities = entity_detection(self._text)
        return [m(tokenized) for m in methods]
        

def basic_processing(text:str) -> str:
    ''' basic processing of the text article
    its converting text to lower case, removed punctuation
    '''
    text = text.lower().strip()
    table = text.maketrans(dict.fromkeys(string.punctuation))
    return text.translate(table)

def remove_stopwords(tokens:List[str]) -> List[str]:
    ''' remove stop words from text
        and return string representation without
        these words
    '''
    stop_words = set(stopwords.words('english'))
    return [w for w in tokens if w not in stop_words]

def stemming(tokens: List[str]) -> List[str]:
    ''' stemmign for words
        for example types -> type
    '''
    stemmer = PorterStemmer()
    return [stemmer.stem(w) for w in tokens]

def ner(tokens: List[str]) -> List[str]:
    '''
    Named enttity recognition returns position tags on text
    '''
    return ne_chunk(pos_tag(tokens))

def entity_detection(text:str):
    nlp = spacy.load("en_core_web_sm")
    data = nlp(text)
    for d in data.ents:
        print(d.lemma_)
    return [(i, i.label_, i.label) for i in data.ents]


