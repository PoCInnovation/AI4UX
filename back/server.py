import flask
import tempfile
import numpy as np
import requests as http

from PIL import Image
from flask import request

from color import dataColor
from models import Model, Conv2D
from screen_page import screen_web_page
from clutter import get_interaction_clutter
from responsive import responsiveness_tester
from analysis import speedtest, horizontal_scroll, headers_consistency, read_page

app = flask.Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return "200"


@app.route("/analyze/speedtest", methods=['GET'])
def analyze_speedtest():
    url: str = request.args.get("url")

    try:
        http.head(url)
        browser_score, mobile_score = speedtest(url)

        response = {
            "mobile": mobile_score,
            "browser": browser_score
        }

        return response
    except Exception as e:
        print("ERROR:", e)
        return 'wrong url', 404


@app.route("/analyze/horizontal_scroll", methods=["GET"])
def analyze_horizontal_scroll():
    url: str = request.args.get("url")
    return str(horizontal_scroll(url))

@app.route("/analyze/headers_consistency", methods=["GET"])
def analyze_headers_consistency():
    url: str = request.args.get("url")
    return headers_consistency(url)

@app.route("/analyze/keypoint", methods=["GET"])
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
    colorNumber, colorBlind, paddingRight, paddingLeft, mainColors = dataColor(img)
    temp.close()

    return {"colorNumber": colorNumber, "colorBlind": colorBlind, "paddingRight": paddingRight, "paddingLeft": paddingLeft, "mainColors": mainColors}

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

    return {
        "all_result": [
            speedtest_result["mobile"],
            speedtest_result["browser"],
            float(scroll_result),
            hearders_result["nb_h1"], # ''
            hearders_result["inconsistencies"], # ''
            responsive_result["score"],
            clutter_result["clutterScore"],
            clutter_result["pageLenScore"],
            colors_result["colorNumber"],
            colors_result["colorBlind"],
            colors_result["paddingRight"],
            colors_result["paddingLeft"],
            colors_result["mainColors"],
            keypoint_result
            ]
         }


@app.route("/model/train", methods=["GET"])
def train_model():
    url: str = request.args.get("url")
    results = analyse_run()
    scores = [np.tanh(scr) for scr in results["all_result"][:12]]

    model = Model(Conv2D)
    model.load("./conv2d.torch")
    temp = tempfile.NamedTemporaryFile()
    screen_web_page(url, (1920, 1080), temp.name)
    pred = model.train(Image.open(temp.name), scores)
    model.save("./conv2d.torch")
    temp.close()

    return {"predictions": pred, "result": results}

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
