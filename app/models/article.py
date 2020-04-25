class Article:
    '''
    Article class to define Article Objects
    '''
    def __init__(self, author, title, description, url, publishedAt, content):
        self.author= author
        self.title= title
        self.description=description
        self.url= url
        self.publishedAt= publishedAt
        self.content= content