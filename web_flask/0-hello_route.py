#!/home/marvel/wurd/pythonLearning/Flask/web_flask/bin/python3
""" starts a flask web application """
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

if __name__ == "__main__":
    app.run()
