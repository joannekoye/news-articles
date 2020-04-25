class Config:
    '''
    General configuration parent class
    '''
    TOP_HEADLINES_URL='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    EVERYTHING_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    SOURCES_URL='https://newsapi.org/v2/sources?apiKey={}'
    CATEGORY_URL='https://newsapi.org/v2/sources?category={}&apiKey={}'
    LANGUAGE_URL='https://newsapi.org/v2/sources?language={}&apiKey={}'
    SEARCH_URL='https://newsapi.org/v2/everything?sources={}&q={}&apiKey={}'


class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
