import flask
import requests as http

from flask import request
from flask_cors import CORS, cross_origin

from analysis import speedtest, horizontal_scroll, headers_consistency, read_page

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return "200"


@app.route("/analyze/speedtest", methods=['GET'])
@cross_origin()
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


@app.route("/analyze/horizontal_scroll", methods=["GET"])
@cross_origin()
def analyze_horizontal_scroll():
    url: str = request.args.get("url")
    return str(horizontal_scroll(url))


@app.route("/analyze/headers_consistency", methods=["GET"])
def analyze_headers_consistency():
    url: str = request.args.get("url")
    return headers_consistency(url)


@app.route("/analyze/keypoint", methods=["GET"])
@cross_origin()
def analyse_keypoint():
    url: str = request.args.get("url")

    browser_words = read_page(url, (1920, 1080))
    mobile_words = read_page(url, (320, 480))

    return {
        "browser": browser_words,
        "mobile": mobile_words
    }


app.run(host="0.0.0.0")
