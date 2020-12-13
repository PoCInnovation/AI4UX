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

## IMAGE ##
image = PIL.Image.open("web_screenshot.png")
width, height = image.size
total = width * height
above, score_dalto = nbColor_daltonisme(image, total)
print(f"\nNombre de couleurs principales : {above} ; Score daltonisme : {score_dalto:.2f}")

## FIRST QUARTER ##
image_first = new_image(image, 0, 0, width // 4, height)
size_first_w, size_first_h = image_first.size
total_first = size_first_w * size_first_h
print(f"\nTotal de vide à gauche : {padding_ratio(image_first, total_first):.2f}%")

## FORTH QUARTER ##
image_forth = new_image(image, (width // 4) * 3, 0, width, height)
size_forth_w, size_forth_h = image_forth.size
total_forth = size_forth_w * size_forth_h
print(f"\nTotal de vide à droite : {padding_ratio(image_forth, total_forth):.2f}%")