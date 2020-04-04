class Article:
    ''' saving of article to elastic search format
    '''
    def __init__(self, text):
        self.text = text
        self.datetime = datetime.datetime.now()
    
    def to_json(self):
        return {}