#!/usr/bin/env python3
""" basic Babel object set up"""
from flask_babel import Babel
app = __import__("0-app").app


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)
