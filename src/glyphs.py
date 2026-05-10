import numpy as np
from PIL import (
    Image,
    ImageDraw,
    ImageFont
)

from random import choice

from setup import setup
from utils import (
    resize,
    show_and_save
)

ARGS = setup('glyphs')

if ARGS['by'] == 'tiles':
    ARGS['image_width'] *= ARGS['font_size'] + ARGS['font_padding']
    ARGS['image_width'] += ARGS['font_padding']

    ARGS['image_height'] *= ARGS['font_size'] + ARGS['font_padding']
    ARGS['image_height'] += ARGS['font_padding']

# Create canvas
image = Image.fromarray(np.full(
    (ARGS['image_height'], ARGS['image_width'], 3),
    ARGS['background_color'],
    np.uint8
))

colors = ARGS['colorset']
glyphs = ARGS['glyphset']

# Setup font
draw = ImageDraw.Draw(image)
draw.fontmode = '1' if ARGS['font_aliasing'] else '0'

font = None
try:
    font = ImageFont.truetype(
        ARGS['font_name'],
        ARGS['font_size']
    )
except OSError:
    print(f"Font {ARGS['font_name']} doesn't found, aborting")
    exit(0)

# Draw glyphs
random_order = ARGS['random_order']
chars = []
if not random_order:
    for i in range(len(glyphs)):
        chars.append(glyphs[i])
char_index = 0

for x in range(
        ARGS['font_padding'],
        ARGS['image_width'],
        ARGS['font_size'] + ARGS['font_padding']
    ):
    for y in range(
            ARGS['font_padding'],
            ARGS['image_height'],
            ARGS['font_size'] + ARGS['font_padding']
        ):
        draw.text(
            xy=(y + ARGS['font_size']//2, x + ARGS['font_size']//2),
            text=choice(glyphs) if random_order else chars[char_index % len(chars)],
            font=font,
            fill=choice(colors),
            anchor='mm'
        )
        char_index += 1 if ARGS['random_order'] != [] else 0

image = resize(
    image,
    ARGS['image_width'] * ARGS['image_scale_factor'],
    ARGS['image_height'] * ARGS['image_scale_factor']
)

show_and_save(image, ARGS['output'], ARGS['quiet'])
