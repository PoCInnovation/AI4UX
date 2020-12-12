import flask
import requests as http

from flask import request
from analysis import Analyzer

app = flask.Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return ""


@app.route("/analyze", methods=['GET'])
def analyze():
    url: str = request.args.get("url")

    print(url)
    try:
        http.head(url)
        a = Analyzer(url)

        browser_score, mobile_score = a.speedtest()

        response = {
            "performance": {
                "mobile": mobile_score,
                "browser": browser_score
            }
        }

        return response
    except Exception:
        return 'wrong url', 404


app.run()
