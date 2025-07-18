#!/usr/bin/env python3
"""Module for a basic Flask app"""

from flask import Flask, render_template
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
def index():
    """Basic function that return a basic template"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
