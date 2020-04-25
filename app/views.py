from flask import render_template
from app import app
from .requests import get_top_headlines, get_sources, get_by_language, get_by_category

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    top_headlines = get_top_headlines()
    sources = get_sources()

    title = 'NEWS-ARTICLES curates the world\'s stories so you can focus on investing in yourself, staying informed, and getting involved.'
    return render_template('index.html', title= title, headlines = top_headlines, sources= sources )


@app.route('/source/<id>')
def source(id):
    return render_template('source.html', id = id)