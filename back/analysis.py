from html.parser import HTMLParser
import requests
import json
import socket
import ssl
from selenium import webdriver
import datetime
import urllib.parse

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


def horizontal_scroll(url: str) -> int:
    """ True if there is a horizontal scroll on the page
    """
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.get(url)
    js = 'return document.documentElement.scrollWidth>document.documentElement.clientWidth;'
    res = driver.execute_script(js)
    return int(res)


class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.headers = []
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag.strip() in ["h1", "h2", "h3", "h4", "h5", "h6"] and len(attrs):
            self.headers.append(tag.strip())


def headers_consistency(url: str) -> Tuple[int, int]:
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.get(url)
    page = driver.page_source
    nb_h1 = page.count("<h1")
    parser = MyHTMLParser()
    parser.feed(page)
    anomaly = 0
    for i in range(len(parser.headers) - 1):
        if int(parser.headers[i][1]) - int(parser.headers[i+1][1]) > 1:
            anomaly += 1
    return {"nb_h1": nb_h1, "inconsistencies": anomaly}


def ssl_expiry_datetime(hostname):
    ssl_dateformat = r'%b %d %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    context.check_hostname = False

    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    conn.settimeout(5.0)

    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    if str(ssl_info).find(hostname) == -1:
        return False
    return datetime.datetime.strptime(ssl_info['notAfter'], ssl_dateformat)


def get_security(url) -> float:
    """
    Check if the given url has a ssl certificate and use https.
    :return: 0 if there is no SSL, 5 if the name in the SSL is wrong
    and 10 if there is a SSL certificate with the good name
    """
    parsed_url = urllib.parse.urlparse(url)
    now = datetime.datetime.now()
    try:
        expire = ssl_expiry_datetime(parsed_url.netloc)
        if expire == False:
            return 5
        diff = expire - now
        days_left = str(diff).split()
        if int(days_left[0]) > 0:
            ssl_validity = True
        else:
            ssl_validity = False
        if ssl_validity == True:
            return 10
        else:
            return 0
    except Exception as e:
        return 0
