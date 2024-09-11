#!/usr/bin/env python3
""" instamtiate Babel object"""
from flask import request
from flask_babel import Babel
app = __import__("0-app").app


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

def get_locale:
    return request.accept_languages.best_match(app.config["LANGUAGES"])

babel = Babel(app, local_selector=get_locale)
