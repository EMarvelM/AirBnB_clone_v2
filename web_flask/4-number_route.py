#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
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


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    Route handler for the C text URL ("/c/<text>").

    Parameters:
        text (str): The text provided in the URL.

    Returns:
        str: A modified string prepended with "C ".
    """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """
    Route handler for the C text URL ("/python/<text>").

    Parameters:
        text (str): The text provided in the URL.

    Returns:
        str: A modified string prepended with "Python ".
    """
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def n_number(n):
    """
    Route handler for the number URL ("/python/<n>").

    Parameters:
        n (int): The number provided provided in the URL.

    Returns:
        str: A string n is a number ".
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run()
