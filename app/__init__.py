from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#Initialize app
app = Flask(__name__, instance_relative_config=True)

#Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#initializing Flask extensions
bootstrap = Bootstrap(app)

from app import views
from app import error

