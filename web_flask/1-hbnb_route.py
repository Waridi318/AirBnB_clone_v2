#!/usr/bin/python3

"""
This module start a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb"""
    return("HBNB")


@app.route('/', strict_slashes=False)
def hello():
    """root"""
    return ("Hello HBNB!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
