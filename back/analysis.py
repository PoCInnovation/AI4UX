import requests
import json
import socket
import ssl
from selenium import webdriver
import datetime
import urllib.parse
import cv2
import pytesseract
import string
import enchant

from screen_page import screen_web_page

from typing import Tuple


language = enchant.Dict('en_US')


def read_page(url: str, size: Tuple[int, int]) -> [str]:
    """ Read page content and return an array of keywords """
    screen_web_page(url, (size[0], size[1]), 'output.png')
    img = cv2.imread('output.png')
    custom_config = r'--oem 3 --psm 6'
    res = pytesseract.image_to_string(img, config=custom_config)

    words = res.split(' ')
    real_words = list(
        filter(lambda word: word is not None, [word.strip() if len(word) > 3 else None for word in words]))

    keyword = list()
    for word in real_words:
        word = word.replace('\n', '')
        filtered_string = list(filter(lambda x: x in string.printable, word))
        word = "".join(filtered_string)
        if (language.check(word) and len(word) > 4) or word[0].isupper():
            word = word.split(',')
            for w in word:
                if len(w) > 3:
                    keyword.append(w)
    return keyword


def speedtest(url: str) -> Tuple[float, float]:
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


def horizontal_scroll(url: str) -> bool:
    """ True if there is a horizontal scroll on the page """
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.get(url)
    js = 'return document.documentElement.scrollWidth>document.documentElement.clientWidth;'
    res = driver.execute_script(js)
    return int(res)


def ssl_expiry_datetime(hostname: str):
    """ Verify ssl """
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


def get_security(url: str) -> float:
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
