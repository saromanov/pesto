import string
import nltk

def basic_processing(text:str):
    ''' basic processing of the text article
    its converting text to lower case, removed punctuation
    '''
    text = text.to_lower().strip()
    return text.translate(string.maketrans("",""), string.punctuation)

