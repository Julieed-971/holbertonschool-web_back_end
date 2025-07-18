#!/usr/bin/env python3
"""Module for a basic Flask app"""

from flask import Flask
from flask_babel import Babel


class Config:
    """Configuration for available languages in app"""
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
babel = Babel(app,
              locale_selector=Config.LANGUAGES[0],
              timezone_selector='UTC')


@app.route("/")
def hello():
    """Basic function that return a basic template"""
    return "<title>Welcome to Holberton</title><h1>Hello world</h1>"
