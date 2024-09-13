#!/usr/bin/env python3
""" mock a user login system """
from flask import Flask, request, render_template

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    retrieves a user_id from request url
    and retrieves a user with the id from a dict.
    """
    user_id = request.args.get("login_as")
    user = users.get(user_id)
    return user


@app.before_request
def before_request():
    """
    This function runs before each request.
    It attempts to get a user using the get_user function and stores
    the user in flask.g so that it is accessible globally in the request.
    """
    user = get_user()
    g.user = user


@app.route("/")
def home():
    return render_template("5-index.html", user=g.user)


if __name__ == "__main__":
    app.run()
