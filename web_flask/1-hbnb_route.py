#!/usr/bin/python3
"""starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL ("/").

    Returns:
        str: A greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the hbnb URL ("/hbnb").

    Returns:
        str: A greeting message "HBNB".
    """
    return "HBNB"


if __name__ == "__name__":
    app.run()
