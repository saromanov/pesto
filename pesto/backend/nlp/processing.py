import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemming

def basic_processing(text:str) -> str:
    ''' basic processing of the text article
    its converting text to lower case, removed punctuation
    '''
    text = text.to_lower().strip()
    return text.translate(string.maketrans("",""), string.punctuation)

def remove_stopwords(text: str) -> str:
    ''' remove stop words from text
        and return string representation without
        these words
    '''
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    return ''.join([w for w in tokens if w not in stop_words])

def stemming(text: str) -> str:
    ''' stemmign for words
        for example types -> type
    '''
    stemmer = PorterStemming()
    tokens = word_tokenize(text)
    return ''.join(stemmer.stem(w) for w in tokens)

