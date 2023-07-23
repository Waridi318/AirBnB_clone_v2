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


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """c is fun"""
    text = text.replace('_', ' ')
    return (f'C {text}')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonisfun(text='is_cool'):
    """python is fun"""
    text = text.replace('_', ' ')
    return (f"Python {text}")


@app.route('/number/<int:n>', strict_slashes=False)
def displaynumber(n):
    """function displays integer only"""
    return (f"{n} is a number")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
