import flask
import tempfile
import numpy as np
import requests as http

from flask_cors import CORS, cross_origin

from PIL import Image
from flask import request

from color import dataColor
from models import Model, Conv2D
from screen_page import screen_web_page
from clutter import get_interaction_clutter
from responsive import responsiveness_tester
from analysis import speedtest, horizontal_scroll, headers_consistency, read_page, get_security

app = flask.Flask(__name__)
CORS(app)


def home():
    return "200"


def analyse_security(url):
    return get_security(url)


def analyze_speedtest(url):
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
        return {
            "mobile": 0.5,
            "browser": 0.5
        }


def analyze_horizontal_scroll(url):
    return str(horizontal_scroll(url))


def analyze_headers_consistency(url):
    return headers_consistency(url)


def analyse_keypoint(url):

    browser_words = read_page(url, (1920, 1080))
    mobile_words = read_page(url, (320, 480))

    return {
        "browser": browser_words,
        "mobile": mobile_words
    }


def analyse_responsive(url):
    score = responsiveness_tester(url)

    return {"score": score}


def analyse_clutter(url):
    clutterScore, pageLenScore = get_interaction_clutter(url)

    return {"clutterScore": clutterScore, "pageLenScore": pageLenScore}


def analyse_colors(url):
    temp = tempfile.NamedTemporaryFile()
    screen_web_page(url, (1920, 1080), temp.name)
    img = Image.open(temp.name)
    colorNumber, colorBlind, paddingRight, paddingLeft, mainColors = dataColor(img)
    temp.close()

    return {"colorNumber": colorNumber, "colorBlind": colorBlind, "paddingRight": paddingRight,
            "paddingLeft": paddingLeft, "mainColors": mainColors}


def analyse_run():
    url: str = request.args.get("url")

    speedtest_result = analyze_speedtest(url)
    scroll_result = analyze_horizontal_scroll(url)
    headers_result = analyze_headers_consistency(url)
    keypoint_result = analyse_keypoint(url)
    clutter_result = analyse_clutter(url)
    responsive_result = analyse_responsive(url)
    colors_result = analyse_colors(url)
    security_result = analyse_security(url)

    print(scroll_result)
    print(headers_result)
    print(keypoint_result)
    print(responsive_result)
    print(clutter_result)
    print(colors_result)

    return {
        "all_result": [
            speedtest_result["mobile"],
            speedtest_result["browser"],
            float(scroll_result),
            headers_result["nb_h1"],  # ''
            headers_result["inconsistencies"],  # ''
            responsive_result["score"],
            clutter_result["clutterScore"],
            clutter_result["pageLenScore"],
            colors_result["colorNumber"],
            colors_result["colorBlind"],
            colors_result["paddingRight"],
            colors_result["paddingLeft"],
            colors_result["mainColors"],
            keypoint_result,
            security_result
        ]
    }


@app.route("/model/train", methods=["GET"])
@cross_origin()
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
@cross_origin()
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
