from random import randint

from PIL import Image, ImageDraw

RESIZE_TO = (512*2, 256*2)

red = (227, 81, 0)
blue = (97, 162, 255)

image = Image.open('./enemies/card.png').convert('RGBA')
draw = ImageDraw.Draw(image)
faces = Image.open('./enemies/faces.png').convert('RGBA')
numbers = Image.open('./enemies/numbers.png').convert('RGBA')
effects = Image.open('./enemies/effects.png').convert('RGBA')

x = randint(0, 30)*16
face = faces.crop((x, 0, x+16, 16))
image.paste(face, (0, 0), face)

# hp
max_hp = randint(10, 100)
hp = max_hp - randint(1, max_hp - 1)
x, y = 11, 3
draw.rectangle((10, 2, 10+int((hp/max_hp)*36), 2+6), fill=red)
hp_text = str(hp) + '/' + str(max_hp)
for i in hp_text:
    glyph = numbers.crop((int(i)*4, 0, int(i)*4+4, 5)) if i != '/' else numbers.crop((10*4, 0, 10*4+4, 5))
    image.paste(glyph, (x, y), glyph)
    x += 4

# mana
max_mana = randint(10, 50)
mana = max_mana - randint(1, max_mana - 1)
x, y = 11, 11
draw.rectangle((10, 10, 10+int((mana/max_mana)*36), 10+6), fill=blue)
mana_text = str(mana) + '/' + str(max_mana)
for i in mana_text:
    glyph = numbers.crop((int(i)*4, 0, int(i)*4+4, 5)) if i != '/' else numbers.crop((10*4, 0, 10*4+4, 5))
    image.paste(glyph, (x, y), glyph)
    x += 4

# level
x, y = 1, 11
level_text = str(randint(1, 25))
for i in level_text:
    glyph = numbers.crop((int(i)*4, 0, int(i)*4+4, 5))
    image.paste(glyph, (x, y), glyph)
    x += 4

# effects
effects_str = ''
x, y = 10, 18
if randint(1, 6) >= 2:
    effects_list = ['0', '1', '2', '3', '4', '5']
    for _ in range(randint(1, 6)):
        effects_str += effects_list.pop(randint(0, len(effects_list)-1))
    for i in effects_str:
        glyph = effects.crop((int(i)*4, 0, int(i)*4+4, 4))
        image.paste(glyph, (x, y), glyph)
        x += 5

image = image.resize(RESIZE_TO, resample=Image.Resampling.BOX)
image.save('image.png')
image.show()
