#!/usr/bin/python3

from flask import Flask, render_template
from models import storage


app = Flask(__name__)
states = storage.all(State)
sorted_states = sorted(states.values(), key=lambda state: state.name)


@app.teardown_appcontext
def teardown_app():
    """removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """displays a HTML page containing a list of States"""
    return (render_template('7-states_list.html'), states=sorted_states)


if '__name__' == '__main__':
    app.run(host='0.0.0.0', port=5000)
