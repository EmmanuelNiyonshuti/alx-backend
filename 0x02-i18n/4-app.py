#!/usr/bin/env python3
"""  Force locale with URL parameter """
from flask import Flask, request, render_template
from flask_babel import Babel
app = __import__("0-app").app
Config = __import__("1-app").Config

app = Flask(__name__)

app.config.from_object(Config)
# Using @babel.localeselector is deprecated, but required for this project:
@babel.localeselector
def get_locale():
    """ get_locale function """
    lang = request.args.get("locale")
    if lang in app.config["LANGUAGES"]:
        return lang
    return request.accept_languages.best_match(app.config["LANGUAGES"])

# babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def home():
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
