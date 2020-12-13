##
## EPITECH PROJECT, 2020
## AI4UX
## File description:
## clutter.py
##

import requests as http
import math
from requests_html import HTMLSession

#removes everything outside the html tags
def light_strip_flags(page):
    flags = ""
    flag = False
    for letter in page:
        if (letter == '<'):
            flag = True
        if (flag):
            flags += letter
        if (letter == '>'):
            flag = False
    return flags

#removes everything outside the html tags as well as the contents of the closing tags
def strip_flags(page):
    flags = ""
    flag = False
    for letter in page:
        if (letter == '<'):
            flag = True
        if (flag and (letter == '/' or letter == ' ')):
            flag = False
            flags += '>'
        if (flag):
            flags += letter
        if (letter == '>'):
            flag = False
    return flags

#counts the values for each flags
def count_flags(flags):
    count = 0
    checked = ["<input>", "<a>", "<button>", "<textarea>", "<select>", "<option>", "<area>", "<video>", "<audio>"]
    for flag in checked:
        count += flags.count(flag)
    return count

#counts the number of html interaction flags
def count_interactions(page) -> int:
    flags = strip_flags(page)
    count = count_flags(flags)
    return count

#gets all the href links in a webpage
def getLinks(tmp):
    links = []
    tmp = light_strip_flags(tmp)
    status = tmp.find("href=\"http")
    page = tmp[(status + 6):]
    while (status >= 0):
        links.append(page[:page.find("\"")])
        page = page[page.find("\""):]
        status = page.find("href=\"http")
        page = page[(status + 6):]
    status = tmp.find("href=\"/url?q=")
    page = tmp[(status + 13):]
    while (status >= 0):
        links.append(page[:page.find("\"")])
        page = page[page.find("\""):]
        status = page.find("href=\"/url?q=")
        page = page[(status + 13):]
    return links

#calculates a page length ratio in comparison to a window
def getHeightRatio(url):
    session = HTMLSession()
    script = """
        () => {
            return {
                scroll: document.body.scrollHeight,
                height: document.documentElement.clientHeight,
            }
        }
    """
    r = session.get(url)
    try:
        val = r.html.render(script = script)
        if (val["height"] != 0):
            return val["scroll"] / val["height"]
        else:
            return 1.0
    except:
        return 1.0

# gets data from current page and calls recursively all the links on the page (if depth > 0)
def reqLink(url, depth):
    text = http.get(url).text
    count = []
    ratioArr = []
    if (depth > 0):
        links = []
        links = getLinks(text)
        for i in links:
            req = []
            req, rat = reqLink(i, depth - 1)
            count.extend(req)
            ratioArr.extend(rat)
    res = count_interactions(text)
    ratio = getHeightRatio(url)
    fin = res
    if (ratio != 0):
        fin = res / ratio
    print(fin, ratio)
    count.append(fin)
    ratioArr.append(ratio)
    return(count, ratioArr)

#calculates the average value of a file
def fileAvg(file):
    f = open(file, "r")
    arr = f.read().split(',')
    ttl = 0
    for i in arr:
        ttl += float(i)
    avg = (ttl / len(arr))
    ttlsq = 0
    for i in arr:
        ttlsq += (float(i) - avg) * (float(i) - avg)
    avgsq = (ttlsq / len(arr))
    return avg, math.sqrt(avgsq)

#gets the biggest and smallest value in a file
def getExtremes(file):
    f = open(file, "r")
    arr = []
    for i in (f.read().split(',')):
        arr.append(float(i))
    myMin = arr[0]
    myMax = arr[0]
    for i in arr:
        if (i < myMin):
            myMin = i
        if (i > myMax):
            myMax = i
    return myMin, myMax

#calculates clutterScore and pageLenScore
def calcClutterScore(div, ratio):
    dataAvg, dataDev = fileAvg("data")
    ratioAvg, ratioDev = fileAvg("ratios")
    dataMin, dataMax = getExtremes("data")
    _, ratioMax = getExtremes("ratios")
    clutterScore = 0
    ratioScore = 0
    if (div > dataMax or div < dataMin):
        clutterScore = 0
    elif (div > dataAvg and div < (dataAvg + dataDev)):
        clutterScore = 1 - (((div - dataAvg) / dataDev) * 0.5)
    elif (div < dataAvg and div > (dataAvg - dataDev)):
        clutterScore = 1 - (((dataAvg - div) / dataDev) * 0.5)
    elif (div > dataAvg + dataDev):
        clutterScore = 1 - (((div - dataAvg + dataDev) / (dataMax - dataAvg + dataDev)) * 0.5 + 0.5)
    elif (div < dataAvg - dataDev):
        clutterScore = 1 - (((dataAvg - dataDev - div) / (dataAvg - dataDev - dataMin)) * 0.5 + 0.5)
    else:
        clutterScore = 1

    if (ratio > ratioMax):
        ratioScore = 0
    elif (ratio < 1):
        ratioScore = ratio
    elif (ratio > ratioAvg and ratio < (ratioAvg + ratioDev)):
        ratioScore = 1 - (((ratio - ratioAvg) / ratioDev) * 0.5)
    elif (ratio > ratioAvg + ratioDev):
        ratioScore = 1 - (((ratio - ratioAvg + ratioDev) / (ratioMax - ratioAvg + ratioDev)) * 0.5 + 0.5)
    else:
        ratioScore = 1
    #ratio score is not pertinent here because average definitely != good. the unit of measurement of the ratio is: 1 = size of the window
    #its score should only lower for values bigger than average (done)

    return clutterScore, ratioScore

#main function to calculate the score
#extra: should add the calculated values to the data files
def get_interaction_clutter(url) -> float:
    """
    give a score to how cluttered interactions are
    """
    text = http.get(url).text
    count = count_interactions(text)
    ratio = getHeightRatio(url)
    div = count
    if (ratio != 0):
        div = count / ratio
    print(div, ratio)
    return(calcClutterScore(div, ratio))

if __name__ == "__main__":
    clutterScore, pageLenScore = get_interaction_clutter("https://www.google.com/search?hl=en&sxsrf=ALeKk03y8oKG1qvCUB1gsakPjE3Ksqfv1g%3A1607802022466&source=hp&ei=phzVX_G3GfLYgwelpLOQCQ&iflsig=AINFCbYAAAAAX9UqthSeRvg2zJVY2HsmqApgtNBj96p1&q=ecommerce&oq=ecommerce&gs_lcp=CgZwc3ktYWIQA1DXHVjFL2DWMGgAcAB4AIABAIgBAJIBAJgBAKABAaoBB2d3cy13aXqwAQA&sclient=psy-ab&ved=0ahUKEwjxoqmjmcntAhVy7OAKHSXSDJIQ4dUDCAY&uact=5")
    print(clutterScore, pageLenScore)

# call function on a a page url
# returns two scores from 0 to 1
#    clutterScore: how cluttered is the page? are there buttons everywhere?
#    pageLenScore: is the page's length appropriate? if the page is smaller than one window or bigger than the average the score lowers.
