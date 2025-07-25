#!/usr/bin/env python3
"""Module for a basic Flask app"""

from datetime import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from pytz import timezone, exceptions

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration for available languages in app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale() -> str:
    """Get the best match locale language"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    # locale from user settings
    user = get_user()
    if user:
        locale = user['locale']
        if locale and locale in app.config['LANGUAGES']:
            return locale
    # locale from request header
    locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if locale:
        return locale
    return app.config['BABEL_DEFAULT_LOCALE']


def get_user() -> dict | None:
    """Return a user dict"""
    login_as = request.args.get("login_as")
    if not login_as:
        return None
    user_id = int(login_as)
    if user_id and user_id in users:
        return users[user_id]
    return None


@app.before_request
def before_request():
    """Find a user and set it as a global"""
    user = get_user()
    if user:
        g.user = user


def is_valid_timezone(time_zone):
    """Check if is a valid time zone"""
    try:
        timezone(time_zone)
        return time_zone
    except exceptions.UnknownTimeZoneError:
        return None


def get_timezone() -> str:
    """Get the best match timezone"""
    # Find timezone parameter in URL parameters
    time = is_valid_timezone(request.args.get('time'))
    if time:
        return time
    # Find time zone from user settings
    user = get_user()
    if user:
        time = is_valid_timezone(user['timezone'])
        if time:
            return time
    return app.config['BABEL_DEFAULT_TIMEZONE']


babel.init_app(
    app,
    locale_selector=get_locale,
    timezone_selector=get_timezone)


@app.route("/")
def index() -> str:
    """Basic function that return a basic template"""
    current_time = datetime.now()
    return render_template("index.html",
                           current_time=current_time,
                           format_datetime=format_datetime)


if __name__ == "__main__":
    app.run()
