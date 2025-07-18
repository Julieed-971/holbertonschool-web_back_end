#!/usr/bin/env python3
"""Module for a basic Flask app"""

from flask import Flask, request
from flask_babel import Babel


class Config:
    """Configuration for available languages in app"""
    LANGUAGES = ['en', 'fr']


def get_locale():
    """Get the locale language"""
    return app.config['LANGUAGES'][0]
    # return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
babel = Babel(app,
              locale_selector=get_locale,
              timezone_selector='UTC')


@app.route("/")
def hello():
    """Basic function that return a basic template"""
    return "<title>Welcome to Holberton</title><h1>Hello world</h1>"
