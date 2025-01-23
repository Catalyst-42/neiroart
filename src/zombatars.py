from PIL import Image
import numpy as np

from setup import setup
from utils import (
    resize,
    show_and_save,
    limit_or_random
)

ARGS = setup('zombatars')
samples = "img/zombatars"

# Image variants in order of rendering
# 
# Element    | Variants with colors    | Unique variants
#     --     |            --           |        --
# Background | 4 + 1*(18)              | 5
# Skin       | 12                      | 12
# Cloth      | 13                      | 13
# Tidbit     | 10 + 5*(18)             | 15
# Accessory  | 13 + 4*(18)             | 17
# Mustache   | 1 + 24*(18)             | 25
# Hair       | 2 + 15*(18)             | 17
# Eyewear    | 5 + 12*(18)             | 17
# Hat        | 2 + 13*(18)             | 15
#     --     |            --           |        --
# Total      | 179_195_575_333_632_000 | 21_555_787_500

background_id = limit_or_random(ARGS['background'], 1, 5)
background_color = ARGS['background_color']
skin_color = ARGS['skin_color']
cloth_id = limit_or_random(ARGS['cloth'], 0, 12)
tidbit_id = limit_or_random(ARGS['tidbit'], 0, 14)
tidbit_color = ARGS['tidbit_color']
accessory_id = limit_or_random(ARGS['accessory'], 0, 16)
accessory_color = ARGS['accessory_color']
mustache_id = limit_or_random(ARGS['mustache'], 0, 24)
mustache_color = ARGS['mustache_color']
hair_id = limit_or_random(ARGS['hair'], 0, 16)
hair_color = ARGS['hair_color']
eyewear_id = limit_or_random(ARGS['eyewear'], 0, 16)
eyewear_color = ARGS['eyewear_color']
hat_id = limit_or_random(ARGS['hat'], 0, 14)
hat_color = ARGS['hat_color']

def color_template_element(element, color):
    alpha = element.getchannel('A')
    element = element.convert('HSV')

    width, height = element.size
    data = np.array(element)
    
    # Make HSV color shift
    for x in range(height):
        for y in range(width):
            data[x][y][0] = np.array(round(color[0]*256/360))
            data[x][y][1] = np.array(round(color[1]*256/100))

            if data[x][y][2] >= np.array(-round(color[2]*256/100)):
                data[x][y][2] += np.array(round(color[2]*256/100))

            elif data[x][y][2] > np.array(8*256/100):
                data[x][y][2] = np.array(0)

    element = Image.fromarray(data, 'HSV')
    element = element.convert('RGBA')
    element.putalpha(alpha)

    return element


# Background
image = Image.open(f'{samples}/backgrounds/{background_id}.png')
if background_id == 1 and background_color != 1:
    image = color_template_element(
        image, background_color
    )

# Skin
skin = Image.open(f'{samples}/skin.png')
skin = color_template_element(skin, skin_color)
image.paste(skin, (5, 0), skin)

skin = Image.open(f'{samples}/blank.png')
image.paste(skin, (5, 0), skin)

# Cloth
if cloth_id != 0:
    cloth = Image.open(f'{samples}/clothes/{cloth_id}.png')
    image.paste(cloth, (5, 0), cloth)

# Tidbit
if tidbit_id != 0:
    if tidbit_id in (2, 3, 10, 11, 12):
        tidbit = Image.open(f'{samples}/tidbits/{tidbit_id}.png')
        if tidbit_color != 1:
            tidbit = color_template_element(
                tidbit, tidbit_color
            )
    else: 
        tidbit = Image.open(f'{samples}/tidbits/{tidbit_id}.png')
    image.paste(tidbit, (5, 0), tidbit)

# Accessory
if accessory_id != 0:
    if accessory_id in (9, 11, 13, 14):
        accessory = Image.open(
            f'{samples}/accessories/{accessory_id}.png'
        )
        if accessory_color != 1:
            accessory = color_template_element(
                accessory, accessory_color
            )
    else: 
        accessory = Image.open(
            f'{samples}/accessories/{accessory_id}.png'
        )
    image.paste(accessory, (5, 0), accessory)

# Mustache
if mustache_id != 0:
    # Mustache pure color
    mustache = Image.open(f'{samples}/mustaches/{mustache_id}.png')
    if mustache_color != 1:
        mustache = color_template_element(
            mustache, mustache_color
        )
    
    image.paste(mustache, (5, 0), mustache)

    # Mustache black outline
    if mustache_id not in (2, 3, 5, 6, 7, 13, 17, 19, 20):
        mustache = Image.open(f'{samples}/mustaches/{mustache_id}_.png')
        image.paste(mustache, (5, 0), mustache)

# Hair
if hair_id != 0:
    hair = Image.open(f'{samples}/hairs/{hair_id}.png')
    if hair_color != 1:
        hair = color_template_element(
            hair, hair_color
        )
    image.paste(hair, (5, 0), hair)

    if hair_id not in (3, 4, 5, 6, 7, 8, 9, 10, 16):
        hair = Image.open(f'{samples}/hairs/{hair_id}_.png')
        image.paste(hair, (5, 0), hair)

# Eyewear
if eyewear_id != 0:
    eyewear = Image.open(f'{samples}/eyewear/{eyewear_id}.png')
    if eyewear_id not in (13, 14, 15, 16):
        if eyewear_color != 1:
            eyewear = color_template_element(
                eyewear, eyewear_color
            )

        image.paste(eyewear, (5, 0), eyewear)

        eyewear = Image.open(f'{samples}/eyewear/{eyewear_id}_.png')
        image.paste(eyewear, (5, 0), eyewear)

# Hat
if hat_id != 0:
    hat = Image.open(f'{samples}/hats/{hat_id}.png')
    if hat_id == 13:
        image.paste(hat, (5, 0), hat)
    else:
        if hat_color != 1:
            hat = color_template_element(
                hat, hat_color
            )

        image.paste(hat, (5, 0), hat)

        if hat_id not in (2, 4, 5, 10, 12, 14):
            hat = Image.open(f'{samples}/hats/{hat_id}_.png')
            image.paste(hat, (5, 0), hat)

image = image.convert('RGB')
image = resize(
    image,
    180 * ARGS['image_scale_factor'],
    180 * ARGS['image_scale_factor']
)

show_and_save(image, ARGS['output'], ARGS['quiet'])
