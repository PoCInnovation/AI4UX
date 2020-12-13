import extcolors
import PIL

image = PIL.Image.open("web_screenshot.png")
width, height = image.size
total = width * height
protanopie = [] # Ne voit pas le rouge
deutéranopie = [] # Ne voit pas le vert
tritanopie = [] # Ne voit pas le bleu
print("Width : ", width, " ; Height : ", height," ; Total px : ",total)
colors, pixel_count = extcolors.extract_from_path("web_screenshot.png")
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
    print(f'Colors : {color[0]} : {percentage:.2f}% ({color[1]} px)')

print(f'Il y a {above} couleur.s principale.s sur le site')
print(f'Il y a {len(protanopie)} couleur.s que les personnes atteinte de protanopie ne peuvent pas voir')
print(f'Il y a {len(deutéranopie)} couleur.s que les personnes atteinte de deutéranopie ne peuvent pas voir')
print(f'Il y a {len(tritanopie)} couleur.s que les personnes atteinte de tritanopie ne peuvent pas voir')