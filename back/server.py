import flask
import requests as http

from flask import request
from analysis import speedtest

app = flask.Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return "200"


@app.route("/analyze/speedtest", methods=['GET'])
def analyze():
    url: str = request.args.get("url")

    print(url)
    try:
        http.head(url)
        browser_score, mobile_score = speedtest(url)

        response = {
            "mobile": mobile_score,
            "browser": browser_score
        }

        return response
    except Exception:
        return 'wrong url', 404


app.run(host="0.0.0.0")
