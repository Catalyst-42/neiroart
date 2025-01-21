from PIL import (
    Image,
    ImageDraw
)

from random import randint

from setup import setup

ARGS = setup('enemies')

image = Image.open('img/enemies/card.png').convert('RGBA')
draw = ImageDraw.Draw(image)

faces = Image.open('img/enemies/faces.png').convert('RGBA')
numbers = Image.open('img/enemies/numbers.png').convert('RGBA')
effects = Image.open('img/enemies/effects.png').convert('RGBA')

x = randint(0, 30) * 16
face = faces.crop((x, 0, x + 16, 16))
image.paste(face, (0, 0), face)

red = (227, 81, 0)
blue = (97, 162, 255)

# Hp bar
max_hp = randint(10, 100)
hp = max_hp - randint(1, max_hp - 1)
x, y = 11, 3

# Red background
draw.rectangle(
    (10, 2, 10 + int(hp / max_hp * 36), 8),
    fill=(227, 81, 0)  # Red
)

# Hp value
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
max_mana = randint(10, 50)
mana = max_mana - randint(1, max_mana - 1)
x, y = 11, 11

# Blue background
draw.rectangle(
    (10, 10, 10 + mana / max_mana * 36, 16),
    fill=(97, 162, 255)  # Blue
)

# Mana value
mana_text = f'{mana}/{max_mana}'
for i in mana_text:
    glyph = (
        numbers.crop((int(i)*4, 0, int(i)*4 + 4, 5))
        if i != '/' else 
        numbers.crop((10*4, 0, 10*4+4, 5))
    )
    image.paste(glyph, (x, y), glyph)
    x += 4

# Level
x, y = 1, 11
level_text = str(randint(1, 25))
for i in level_text:
    glyph = numbers.crop((int(i)*4, 0, int(i)*4 + 4, 5))
    image.paste(glyph, (x, y), glyph)
    x += 4

# Additional effects
effects_str = ''
x, y = 10, 18
if randint(1, 6) >= 2:
    effects_list = list('012345')

    # Get list of random effects
    for _ in range(randint(1, 6)):
        effects_str += effects_list.pop(
            randint(0, len(effects_list) - 1)
        )
    
    # Display icons of effects
    for i in effects_str:
        glyph = effects.crop((int(i)*4, 0, int(i)*4 + 4, 4))
        image.paste(glyph, (x, y), glyph)
        x += 5

image = image.resize(
    size=(
        48 * ARGS['image_scale_factor'],
        24 * ARGS['image_scale_factor']
    ),
    resample=Image.Resampling.BOX
)

# Display image and save it
if ARGS["output"]:
    try:
        image.save(ARGS["output"])
    except ValueError:
        print(f"Unknown file extension for '{ARGS["output"]}'")
        exit(0)

if not ARGS["quiet"] or not ARGS["output"]:
    image.show()
