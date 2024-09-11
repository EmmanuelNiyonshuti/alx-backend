#!/usr/bin/env python3
""" instamtiate Babel object"""
from config import Config
from flask_babel import Babel
app = __import__("0-app").app


app.config.from_object(Config)

babel = Babel(app)
