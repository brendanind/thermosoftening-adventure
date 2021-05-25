# Main code v1
# Brendan Ind 2021

# Imports
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<html><h1>Hello, World!</h1></html>"


if __name__ == "__main__":
    app.run(debug=True)
