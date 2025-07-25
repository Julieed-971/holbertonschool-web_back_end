#!/usr/bin/env python3
"""Module for a basic Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration for available languages in app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/")
def index() -> str:
    """Basic function that return a basic template"""
    return render_template("2-index.html")


def get_locale() -> str:
    """Get the best match locale language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)

if __name__ == "__main__":
    app.run()
