import extcolors
import PIL

def new_image(image, x1, y1, x2, y2):
    area = (x1, y1, x2, y2)
    tmp = image.crop(area)
    return tmp

def nbColor_daltonisme(image, total):
    protanopie = [] # Ne voit pas le rouge
    deutéranopie = [] # Ne voit pas le vert
    tritanopie = [] # Ne voit pas le bleu
    colors, pixel_count = extcolors.extract_from_image(image)
    above = 0
    for color in colors:
        percentage = color[1] / total * 100
        if percentage > 15:
            above += 1
        if percentage > 5 and color[0][2] > 200 and color[0][0] < 200 and color[0][1] < 200:
            tritanopie.append(color)
        if percentage > 5 and color[0][1] > 200 and color[0][0] < 200 and color[0][2] < 200:
            deutéranopie.append(color)
        if percentage > 5 and color[0][0] > 200 and color[0][1] < 200 and color[0][2] < 200:
            protanopie.append(color)
    return above, (len(protanopie) + len(deutéranopie) + len(tritanopie)) / len(colors)

def padding_ratio(image, total):
    colors, pixel = extcolors.extract_from_image(image)
    i = 0
    total_percent = 0
    percentage = 0
    for color in colors:
        percentage = color[1] / total * 100
        if i < 3:
            total_percent += percentage
            i += 1
    return total_percent

def dataColor(image):
    width, height = image.size
    total = width * height
    above, score_dalto = nbColor_daltonisme(image, total)
    image_first = new_image(image, 0, 0, width // 4, height)
    size_first_w, size_first_h = image_first.size
    total_first = size_first_w * size_first_h
    percent_first = padding_ratio(image_first, total_first)
    image_forth = new_image(image, (width // 4) * 3, 0, width, height)
    size_forth_w, size_forth_h = image_forth.size
    total_forth = size_forth_w * size_forth_h
    percent_forth = padding_ratio(image_forth, total_forth)

    score_color = 1.0
    if above > 3:
        score_color -= 0.15 * (above - 3)
    if score_color < 0.0:
        score_color = 0.0

    return score_color, 1 - score_dalto, round(percent_first) / 100 , round(percent_forth) / 100

## IMAGE ##
image = PIL.Image.open("web_screenshot.png")

print(dataColor(image))