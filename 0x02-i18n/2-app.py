#!/usr/bin.env python3
""" Get locale from requests implementation"""
from flask import request
babel = __import__("1-app").babel


@babel.localeselector
def get_locale():
    """ get_locale function """
    return request.accept_languages.best_match(app.config["LANGUAGES"])
