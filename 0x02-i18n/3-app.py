#!/usr/bin/env python3
""" Parametrize templates """
from flask import request
app = __import__("0-app").app
babel = __import__("1-app").babel


# Using @babel.localeselector is deprecated, but required for this project:
@babel.localeselector
def get_locale():
    """ get_locale function """
    return request.accept_languages.best_match(app.config["LANGUAGES"])

# This is the newer approach, but not used here
# because locale_selector is required:
# babel = Babel(app, locale_selector=get_locale)
