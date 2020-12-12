import requests
import json

from typing import Tuple


class Analyzer:
    """ analyzes various UX KPIs
    """

    def __init__(self, url: str) -> None:
        self.url: str = url

    def get_security(self) -> float:
        """ check security of the given website
        """
        return 0.5

    def speedtest(self) -> Tuple[float, float]:
        """
        Analyse performance of the website thanks to Google API.
        :return: A tuple of performance's rate (browser, mobile)
        """
        browser_res = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?'
                                   'strategy=DESKTOP'
                                   '&url=' + self.url)
        browser_res = json.loads(browser_res.text)
        browser_score = browser_res.get('lighthouseResult').get('categories').get('performance').get('score', None)

        mobile_res = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?'
                                  'strategy=MOBILE'
                                  '&url=' + self.url)
        mobile_res = json.loads(mobile_res.text)
        mobile_score = mobile_res.get('lighthouseResult').get('categories').get('performance').get('score', None)

        return browser_score, mobile_score
