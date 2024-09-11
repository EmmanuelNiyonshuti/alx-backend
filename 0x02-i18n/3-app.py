#!/usr/bin/env python3
""" Parametrize templates """
from flask import Flask, render_template, request
from flask_babel import Babel
Config = __import__("1-app").Config

app = Flask(__name__)

app.config.from_object(Config)

# Using @babel.localeselector is deprecated, but required for this project:
@babel.localeselector
def get_locale():
    """ get_locale function """
    # return "fr"
    return request.accept_languages.best_match(app.config["LANGUAGES"])

# This is the newer approach, but not used here
# because locale_selector is required:
# babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def home():
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)
