import flask
from flask import request
from analysis import Analyzer

app = flask.Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return ""

@app.route("/analyze", methods=['GET'])
def analyze():
    url: str = request.args.get("url")
    a = Analyzer(url)
    return str(a.get_security())

app.run()
