from flask import render_template
from app import app
from .requests import get_top_headlines, get_sources, get_by_language, get_by_category, open_source_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    top_headlines = get_top_headlines()
    sources = get_sources()

    title =' NEWS-ARTICLES - Stay Informed, Get Involved '
    # title = 'NEWS-ARTICLES curates the world\'s stories so you can focus on investing in yourself, staying informed, and getting involved.'
    return render_template('index.html', title= title, headlines = top_headlines, sources= sources )


@app.route('/source/<id>')
def source_articles(id):
    news_articles = open_source_articles(id)
    title = id

    return render_template('source_articles.html', title = title, articles= news_articles)