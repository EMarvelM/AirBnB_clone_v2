#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template

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


@app.route("/number_template/<int:n>", strict_slashes=False)
def n_template(n):
    """
    Route handler for the number URL ("/number_template/<n>").

    Parameters:
        n (int): The number provided provided in the URL.

    Returns:
        str: The html page to render".
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """
    //TODO
    """
    if n % 2:
        oe = "odd"
    else:
        oe = "even"
    return render_template('6-number_odd_or_even.html', n=n, oe=oe)


if __name__ == "__main__":
    app.run()
