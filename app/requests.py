from app import app
import urllib.request, json
from .models import source, article


Source = source.Source
Article = article.Article


#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the urls
top_headlines_url = app.config['TOP_HEADLINES_URL']
everything_url = app.config['EVERYTHING_URL']
sources_url = app.config['SOURCES_URL']
category_url = app.config['CATEGORY_URL']
language_url = app.config['LANGUAGE_URL']
search_url = app.config['SEARCH_URL']

def open_source_articles(source_id):
    '''
    Function that processes a news source and transforms it into an object list

    Args:
        source_id: An id of a specific news source

    Returns:
        source_articles: A list of items in the source object
    
    '''
    get_news_source_url = everything_url.format(source_id, api_key)

    with urllib.request.urlopen(get_news_source_url) as url:
        source_data = url.read()
        source_response = json.loads(source_data)

        source_items = None

        if source_response['articles']:
            source_article_list = source_response['articles']
            source_articles = process_articles(source_article_list)

    return source_articles

def get_top_headlines():
    '''
    Function that gets the json response to our url request
    '''
    get_top_headlines_url= top_headlines_url.format(api_key)

    with urllib.request.urlopen(get_top_headlines_url) as url:
        top_headlines_data = url.read()
        top_headlines_response = json.loads(top_headlines_data)

        new_top_headlines = None

        if top_headlines_response['articles']:
            top_headlines_list = top_headlines_response['articles']
            all_top_headlines_list = process_articles(top_headlines_list)
    
    return all_top_headlines_list


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)

        news_sources = None

        if sources_response['sources']:
            news_sources_list = sources_response['sources']
            news_sources = process_sources(news_sources_list)

    return news_sources



    
def get_by_category(category):
    '''
    Function that gets the json response to our url request
    '''
    get_category_url = category_url.format(category, api_key)

    with urllib.request.urlopen(get_category_url) as url:
        category_data = url.read()
        category_response = json.loads(category_data)

        all_category_sources = None

        if category_response['sources']:
            category_sources_list = category_response['sources']
            all_category_sources = process_sources(category_sources_list)

    return all_category_sources


def get_by_language(language):
    '''
    Function that gets the json response to our url request
    '''
    get_language_url = language_url.format(language, api_key)

    with urllib.request.urlopen(get_language_url) as url:
        language_data = url.read()
        language_response = json.loads(language_data)

        all_language_sources = None

        if language_response['sources']:
            language_sources_list = language_response['sources']
            all_language_sources = process_sources(language_sources_list)

    return all_language_sources


def process_articles(article_list):
    '''
    Function that processes the article result and transforms them to a list of Objects
    
    Args:
        article_list: A list of dictionaries that contain article details

    Returns:
        article_results: A list of article objects
    '''
    article_results = []
    for article in article_list:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        publishedAt = article.get('publishedAt')
        content = article.get('content')

        article_object = Article(author, title, description, url, publishedAt, content)
        article_results.append(article_object)
    
    return article_results


def process_sources(source_list):
    '''
    Function that processes the source result and transforms them to a list of Objects
    
    Args:
        source_list: A list of dictionaries that contain source details

    Returns:
        source_results: A list of article objects
    '''

    source_results = []
    for news_source in source_list:
        id = news_source.get('id')
        name = news_source.get('name')
        description = news_source.get('description')
        url = news_source.get('url')
        category = news_source.get('category')
        language = news_source.get('language')
        country = news_source.get('country')

        source_object= Source(id, name, description,url, category, language, country)
        source_results.append(source_object)

    return source_results





# def search_article(name , source_id):
#     get_search_result_url = search_url.format(source_id, name, api_key)

#     with urllib.request.urlopen(get_search_result_url) as url:
#         search_article_data = url.read()
#         search_article_response = json.loads(search_article_data)

#         search_results = None

#         if search_article_response['articles']:
#             search_list = search_article_response['articles']
#             search_results = process_news(search_list)

#     return search_results