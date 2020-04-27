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


class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self, id, name, description, url, category, language, country):
        self.id= id
        self.name= name
        self.description= description
        self.url= url
        self.category= category
        self.language=language
        self.country=country