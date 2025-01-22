from PIL import (
    Image,
    ImageDraw
)

from math import floor
from random import (
    randint,
    sample
)

from setup import setup
from utils import (
    resize,
    show_and_save,
    limit_or_random
)

ARGS = setup('enemies')

image = Image.open('img/enemies/card.png').convert('RGBA')
draw = ImageDraw.Draw(image)

faces = Image.open('img/enemies/faces.png').convert('RGBA')
numbers = Image.open('img/enemies/numbers.png').convert('RGBA')
effects = Image.open('img/enemies/effects.png').convert('RGBA')

face = (limit_or_random(ARGS['face'], 1, 31) - 1) * 16
face = faces.crop((face, 0, face + 16, 16))
image.paste(face, (0, 0), face)

# Hp bar
max_hp = limit_or_random(ARGS["max_hp"], 1, 999)
hp = limit_or_random(ARGS["hp"], 1, max_hp)

# Red background
draw.rectangle(
    (10, 2, 10 + floor(hp / max_hp * 35), 8),
    fill=(227, 81, 0)  # Red
)

# Hp value
x, y = 11, 3
hp_text = f'{hp}/{max_hp}'
for i in hp_text:
    glyph = (
        numbers.crop((int(i)*4, 0, int(i)*4 + 4, 5))
        if i != '/' else
        numbers.crop((40, 0, 44, 5))
    )
    image.paste(glyph, (x, y), glyph)
    x += 4

# Mana bar
max_mana = limit_or_random(ARGS["max_mana"], 1, 999)
mana = limit_or_random(ARGS["mana"], 0, max_mana)

# Blue background
if mana != 0:
    draw.rectangle(
        (10, 10, 10 + floor(mana / max_mana * 35), 16),
        fill=(97, 162, 255)  # Blue
    )

# Mana value
x, y = 11, 11
mana_text = f'{mana}/{max_mana}'
for i in mana_text:
    glyph = (
        numbers.crop((int(i)*4, 0, int(i)*4 + 4, 5))
        if i != '/' else 
        numbers.crop((40, 0, 44, 5))
    )
    image.paste(glyph, (x, y), glyph)
    x += 4

# Level
x, y = 1, 11
level_text = str(limit_or_random(ARGS['level'], 1, 99))

if len(level_text) == 1:
    x += 2

for i in level_text:
    glyph = numbers.crop((int(i)*4, 0, int(i)*4 + 4, 5))
    image.paste(glyph, (x, y), glyph)
    x += 4

# Additional effects
x, y = 10, 18
effects_str = ARGS['effects'] or (
    sample(list('012345'), randint(0, 6))
)

# Display icons of effects
for i in effects_str:
    glyph = effects.crop((int(i)*4, 0, int(i)*4 + 4, 4))
    image.paste(glyph, (x, y), glyph)
    x += 5

image = resize(
    image,
    48 * ARGS['image_scale_factor'],
    24 * ARGS['image_scale_factor']
)

show_and_save(image, ARGS['output'], ARGS['quiet'])
