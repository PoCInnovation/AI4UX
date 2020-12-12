import requests
import json
import socket
import ssl
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
    except Exception as e:
        return 0
