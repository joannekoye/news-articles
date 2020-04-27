from flask import render_template, request
from . import main
from ..requests import get_top_headlines, get_sources, get_by_language, get_by_category, open_source_articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    top_headlines = get_top_headlines()
    sources = get_sources()

    title =' NEWS-ARTICLES - Stay Informed, Get Involved '

    sort_type = request.args.get('sortBy_query')

    Categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    NewCategories = []
    for Category in Categories:
        category = get_by_category(Category)
        NewCategories.append(category)

    Languages = ['en', 'ar', 'de', 'es', 'fr', 'he', 'it', 'nl', 'no', 'pt', 'ru', 'se', 'ud', 'zh']
    NewLanguages = []
    for Language in Languages:
        language = get_by_language(Language)
        NewLanguages.append(language)

    return render_template('index.html', sources = sources, title = title, Categories = NewCategories, Languages = NewLanguages, sort_type = sort_type, headlines = top_headlines)

@main.route('/source/<id>')
def source_articles(id):
    news_articles = open_source_articles(id)
    title = id

    return render_template('source_articles.html', title = title, articles= news_articles)