#!/usr/bin/env python3
"""Module for a basic Flask app"""

from flask import Flask, request
from flask_babel import Babel


class Config:
    """Configuration for available languages in app"""
    LANGUAGES = ['en', 'fr']
    TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app,
              default_locale=app.config['LANGUAGES'],
              timezone_selector=app.config['TIMEZONE'])
app.config.from_object(Config)


@app.route("/")
def hello():
    """Basic function that return a basic template"""
    return "<title>Welcome to Holberton</title><h1>Hello world</h1>"
