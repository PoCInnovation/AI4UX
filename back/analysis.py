import requests
import json

from typing import Tuple


def speedtest(url) -> Tuple[float, float]:
    """
    Analyse performance of the website thanks to Google API.
    :return: A tuple of performance's rate (browser, mobile)
    """
    browser_res = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?'
                               'strategy=DESKTOP'
                               '&url=' + url)
    browser_res = json.loads(browser_res.text)
    browser_score = browser_res.get('lighthouseResult').get('categories').get('performance').get('score', None)

    mobile_res = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?'
                              'strategy=MOBILE'
                              '&url=' + url)
    mobile_res = json.loads(mobile_res.text)
    mobile_score = mobile_res.get('lighthouseResult').get('categories').get('performance').get('score', None)

    return browser_score, mobile_score


def get_security(url) -> float:
    """ check security of the given website
    :return: Float
    """
    return 0.5

def get_interaction_clutter(url) -> float:
    """
    give a score to how cluttered interactions are
    """
    print(url)
    return 0.5