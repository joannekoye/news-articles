from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'NEWS-ARTICLES curates the world\'s stories so you can focus on investing in yourself, staying informed, and getting involved.'
    return render_template('index.html', title= title)


@app.route('/source/<id>')
def source(id):
    return render_template('source.html', id = id)