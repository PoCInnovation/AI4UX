import os
import requests

def responsiveness_tester(url):
    x = requests.post("https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key="+os.getenv("GOOGLE_API_KEY"), data={"url": url})
    if x.text.find("error")  > 0 or x.text.find("PAGE_UNREACHABLE") > 0:
        return -1
    if x.text.find("MOBILE_FRIENDLY"):
        return 1
    return 0
