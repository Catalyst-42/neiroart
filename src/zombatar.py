from colors import colors_bright, colors_common, colors_skin
from random import randint
from PIL import Image

import numpy as np

RESIZE_TO = (512, 512)

'''
Элемент    | Варианты с цветами      | Уникальные варианты
background | 4+18*(1)                | 5
skin       | 12                      | 12
cloth      | 13                      | 13
tidbit     | 10+18*(5)               | 15
accessory  | 13+18*(4)               | 17
mustache   | 1+18*(24)               | 25
hair       | 2+18*(15)               | 17
eyewear    | 5+18*(12)               | 17
hat        | 2+18*(13)               | 15
Итог       | 179'195'575'333'632'000 | 21'555'787'500
'''

# background -> skin -> cloth -> tidbit -> accessory -> mustache -> hair -> eyewear -> hat
background_id = randint(1, 5); background_color = randint(1, 18)
skin_color = randint(1, 12)
cloth_id = randint(0, 12)
tidbit_id = randint(0, 14); tidbit_color = randint(1, 18)
accessory_id = randint(0, 16); accessory_color = randint(1, 18)
mustache_id = randint(0, 24); mustache_color = randint(1, 18)
hair_id = randint(0, 16); hair_color = randint(1, 18)
eyewear_id = randint(0, 16); eyewear_color = randint(1, 18)
hat_id = randint(0, 14); hat_color = randint(1, 18)

# 3(0)-1-3-0(0)-0(0)-1(10)-0(0)-5(5)-0(0)
# background_id = 3; background_color = 0
# skin_color = 1
# cloth_id = 3
# tidbit_id = 0; tidbit_color = 0
# accessory_id = 0; accessory_color = 0
# mustache_id = 1; mustache_color = 10
# hair_id = 0; hair_color = 0
# eyewear_id = 5; eyewear_color = 5
# hat_id = 0; hat_color = 0

def shift():
    for x in range(height):
        for y in range(width):
            data[x][y][0] = np.array(round(color[0]*256/360))
            data[x][y][1] = np.array(round(color[1]*256/100))
            
            if data[x][y][2] >= np.array(-round(color[2]*256/100)):
                data[x][y][2] += np.array(round(color[2]*256/100))

            elif data[x][y][2] > np.array(8*256/100):
                data[x][y][2] = np.array(0)
            
# pic bg
image = Image.open(f'img/zombatar/backgrounds/{background_id}.png')
if background_id == 1 and background_color != 1:
    alpha = image.getchannel('A'); image = image.convert('HSV')
    width, height = image.size
    data = np.array(image)
    color = colors_bright[background_color-2]
    shift()
    image = Image.fromarray(data, 'HSV'); image = image.convert('RGBA'); image.putalpha(alpha)
else: background_color = 0

# skin
skin = Image.open(f'img/zombatar/skin.png')
alpha = skin.getchannel('A'); skin = skin.convert('HSV')
width, height = skin.size
data = np.array(skin)
color = colors_skin[skin_color-1]
shift()
skin = Image.fromarray(data, 'HSV'); skin = skin.convert('RGBA'); skin.putalpha(alpha)
skin = skin.convert('RGBA'); image.paste(skin, (5, 0), skin)
skin = Image.open(f'img/zombatar/blank.png'); image.paste(skin, (5, 0), skin)

# cloth
if cloth_id != 0:
    cloth = Image.open(f'img/zombatar/clothes/{cloth_id}.png')
    image.paste(cloth, (5, 0), cloth)

# tidbit
if tidbit_id != 0:
    if tidbit_id in (2, 3, 10, 11, 12):
        tidbit = Image.open(f'img/zombatar/tidbits/{tidbit_id}.png')
        if tidbit_color != 1:
            alpha = tidbit.getchannel('A'); tidbit = tidbit.convert('HSV')
            width, height = tidbit.size
            data = np.array(tidbit)
            color = colors_bright[tidbit_color-2]
            shift()
            tidbit = Image.fromarray(data, 'HSV'); tidbit = tidbit.convert('RGBA'); tidbit.putalpha(alpha)
    else: 
        tidbit_color = 0
        tidbit = Image.open(f'img/zombatar/tidbits/{tidbit_id}.png')
    image.paste(tidbit, (5, 0), tidbit)
else: tidbit_color = 0

# accessory
if accessory_id != 0:
    if accessory_id in (9, 11, 13, 14):
        accessory = Image.open(f'img/zombatar/accessories/{accessory_id}.png')
        if accessory_color != 1:
            alpha = accessory.getchannel('A'); accessory = accessory.convert('HSV')
            width, height = accessory.size
            data = np.array(accessory)
            color = colors_bright[accessory_color-2]
            shift()
            accessory = Image.fromarray(data, 'HSV'); accessory = accessory.convert('RGBA'); accessory.putalpha(alpha)
    else: 
        accessory_color = 0
        accessory = Image.open(f'img/zombatar/accessories/{accessory_id}.png')
    image.paste(accessory, (5, 0), accessory)
else: accessory_color = 0

# mustache
if mustache_id != 0:
    mustache = Image.open(f'img/zombatar/mustaches/{mustache_id}.png')
    if mustache_color != 1:
        alpha = mustache.getchannel('A'); mustache = mustache.convert('HSV')
        width, height = mustache.size
        data = np.array(mustache)
        color = colors_common[mustache_color-2]
        shift()
        mustache = Image.fromarray(data, 'HSV'); mustache = mustache.convert('RGBA'); mustache.putalpha(alpha)
    image.paste(mustache, (5, 0), mustache)
    if mustache_id not in (2, 3, 5, 6, 7, 13, 17, 19, 20):
        mustache = Image.open(f'img/zombatar/mustaches/{mustache_id}_.png')
        image.paste(mustache, (5, 0), mustache)
else: mustache_color = 0

# hair
if hair_id != 0:
    hair = Image.open(f'img/zombatar/hairs/{hair_id}.png')
    if hair_id == 3:
        hair_color = 0
        image.paste(hair, (5, 0), hair)
    elif hair_color != 1:
        alpha = hair.getchannel('A'); hair = hair.convert('HSV')
        width, height = hair.size
        data = np.array(hair)
        color = colors_common[hair_color-2]
        shift()
        hair = Image.fromarray(data, 'HSV'); hair = hair.convert('RGBA'); hair.putalpha(alpha)
    image.paste(hair, (5, 0), hair)
    if hair_id not in (3, 4, 5, 6, 7, 8, 9, 10, 16):
        hair = Image.open(f'img/zombatar/hairs/{hair_id}_.png')
        image.paste(hair, (5, 0), hair)
else: hair_color = 0

# eyewear
if eyewear_id != 0:
    eyewear = Image.open(f'img/zombatar/eyewear/{eyewear_id}.png')
    if eyewear_id not in (13, 14, 15, 16):
        if eyewear_color != 1:
            alpha = eyewear.getchannel('A'); eyewear = eyewear.convert('HSV')
            width, height = eyewear.size
            data = np.array(eyewear)
            color = colors_bright[eyewear_color-2]
            shift()
            eyewear = Image.fromarray(data, 'HSV'); eyewear = eyewear.convert('RGBA'); eyewear.putalpha(alpha)
        image.paste(eyewear, (5, 0), eyewear)
        eyewear = Image.open(f'img/zombatar/eyewear/{eyewear_id}_.png')
    else: eyewear_color = 0
    image.paste(eyewear, (5, 0), eyewear)
else: eyewear_color = 0

# hat
if hat_id != 0:
    hat = Image.open(f'img/zombatar/hats/{hat_id}.png')
    if hat_id == 13: 
        hat_color = 0
        image.paste(hat, (5, 0), hat)
    else:
        if hat_color != 1:
            alpha = hat.getchannel('A'); hat = hat.convert('HSV')
            width, height = hat.size
            data = np.array(hat)
            color = colors_bright[hat_color-2]
            shift()
            hat = Image.fromarray(data, 'HSV'); hat = hat.convert('RGBA'); hat.putalpha(alpha)
        image.paste(hat, (5, 0), hat)
        if hat_id not in (2, 4, 5, 10, 12, 14):
            hat = Image.open(f'img/zombatar/hats/{hat_id}_.png')
            image.paste(hat, (5, 0), hat)
else: hat_color = 0

# background -> skin -> cloth -> tidbits -> accessory -> mustache -> hair -> eyewear -> hat
seed = f'{background_id}({background_color})-{skin_color}-{cloth_id}-{tidbit_id}({tidbit_color})-'
seed += f'{accessory_id}({accessory_color})-{mustache_id}({mustache_color})-{hair_id}({hair_color})-'
seed += f'{eyewear_id}({eyewear_color})-{hat_id}({hat_color})'
print('seed:', seed)

image = image.convert('RGB')
image = image.resize(RESIZE_TO, resample=Image.Resampling.BOX)
image.save(f'image.png')
image.show()
