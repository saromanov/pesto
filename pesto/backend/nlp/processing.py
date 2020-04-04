from types import List
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, pos_tag, ne_chunk
from nltk.stem import PorterStemming

class Processing:
    def __init__(self, text:str):
        self._text = text
    
    def do(self):
        processed = basic_processing(self._text)
        tokenized = word_tokenize(self._text)
        methods = [remove_stopwords, stemming, ner]
        return [m(tokenized) for m in methods]
        

def basic_processing(text:str) -> str:
    ''' basic processing of the text article
    its converting text to lower case, removed punctuation
    '''
    text = text.to_lower().strip()
    return text.translate(string.maketrans("",""), string.punctuation)

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
    stemmer = PorterStemming()
    return stemmer.stem(w) for w in tokens

def ner(tokens: List[str]) -> List[str]:
    '''
    Named enttity recognition returns position tags on text
    '''
    return ne_chunk(pos_tag(word_tokenize(input_str)))

