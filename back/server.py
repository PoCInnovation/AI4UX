import flask
import tempfile
import numpy as np
import requests as http

from PIL import Image
from flask import request
from flask_cors import CORS, cross_origin

from analysis import speedtest, horizontal_scroll, headers_consistency, read_page, get_security
from color import dataColor

from models import Model, Conv2D
from screen_page import screen_web_page
from clutter import get_interaction_clutter
from responsive import responsiveness_tester

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return "200"


@app.route('/analyze/security', methods=['GET'])
@cross_origin()
def security():
    url: str = request.args.get("url")
    return str(get_security(url))


@app.route("/analyze/speedtest", methods=['GET'])
@cross_origin()
def analyze_speedtest():
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


@app.route("/analyze/responsive", methods=["GET"])
def analyse_responsive():
    url: str = request.args.get("url")
    score = responsiveness_tester(url)

    return {"score": score}


@app.route("/analyze/clutter", methods=["GET"])
def analyse_clutter():
    url: str = request.args.get("url")
    clutterScore, pageLenScore = get_interaction_clutter(url)

    return {"clutterScore": clutterScore, "pageLenScore": pageLenScore}


@app.route("/analyze/colors", methods=["GET"])
def analyse_colors():
    url: str = request.args.get("url")
    temp = tempfile.NamedTemporaryFile()
    screen_web_page(url, (1920, 1080), temp.name)
    img = Image.open(temp.name)
    colorNumber, colorBlind, paddingRight, paddingLeft = dataColor(img)
    temp.close()

    return {"colorNumber": colorNumber, "colorBlind": colorBlind, "paddingRight": paddingRight,
            "paddingLeft": paddingLeft}


@app.route("/analyze/run", methods=["GET"])
def analyse_run():
    url: str = request.args.get("url")
    speedtest_result = analyze_speedtest()
    scroll_result = analyze_horizontal_scroll()
    hearders_result = analyze_headers_consistency()
    keypoint_result = analyse_keypoint()
    responsive_result = analyse_responsive()
    clutter_result = analyse_clutter()
    colors_result = analyse_colors()
    # clutterScore, pageLenScore = get_interaction_clutter(url)

    return {"TODO1": 0, "TODO2": 0, "TODO3": 0, "TODO4": 0}


@app.route("/model/train", methods=["POST"])
def train_model():
    t_scores = [np.tanh(scr) for scr in request.json['target_scores']]
    t_url = request.json['target_url']
    model = Model(Conv2D)
    model.load("./conv2d.torch")
    temp = tempfile.NamedTemporaryFile()
    screen_web_page(t_url, (1920, 1080), temp.name)
    pred = model.train(Image.open(temp.name), t_scores)
    model.save("./conv2d.torch")
    temp.close()

    return {"predictions": pred}


@app.route("/model/predict", methods=["POST"])
def predict_model():
    temp = tempfile.NamedTemporaryFile()
    t_url = request.json['target_url']
    model = Model(Conv2D)
    model.load("./conv2d.torch")
    screen_web_page(t_url, (1920, 1080), temp.name)
    pred = model.predict(Image.open(temp.name))
    pred = [p * 100 for p in pred[0]]
    temp.close()
    return {"predictions": pred}


app.run(host="0.0.0.0")
