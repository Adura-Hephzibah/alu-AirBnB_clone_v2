#!/usr/bin/python3
"""
Write a script that starts a Flask web application: Your web application must
be listening on 0.0.0.0,
port 5000.
You must use storage for fetching data from the storage engine (FileStorage or
DBStorage) => from models
import storage and storage.all(...)
After each request you must remove the current SQLAlchemy Session:
    - Declare a method to handle @app.teardown_appcontext
    - Call in this method storage.close()
strict_slashes=False in your route definition
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities():
    """display a HTML page”
    """
    return render_template('8-cities_by_states.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
