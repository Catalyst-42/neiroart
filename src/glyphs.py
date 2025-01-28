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

# Create canvas
image = Image.fromarray(np.full(
    (ARGS['image_height'], ARGS['image_width'], 3),
    ARGS['background_color'],
    np.uint8
))

colors = ARGS['glyph_colorset']
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
    print(f"Font '{ARGS['font_name']}' doesn't found, aborting")
    exit(0)

# Draw glyphs
for x in range(
        ARGS['font_margin'],
        ARGS['image_width'],
        ARGS['font_size'] + ARGS['font_margin']
    ):
    for y in range(
            ARGS['font_margin'],
            ARGS['image_height'],
            ARGS['font_size'] + ARGS['font_margin']
        ):
        draw.text(
            xy=(x, y),
            text=choice(glyphs),
            font=font,
            fill=choice(colors)
        )

image = resize(
    image,
    ARGS['image_width'] * ARGS['image_scale_factor'],
    ARGS['image_height'] * ARGS['image_scale_factor']
)

show_and_save(image, ARGS['output'], ARGS['quiet'])
