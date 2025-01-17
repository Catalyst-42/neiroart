from colors import RGB, BLACK
from PIL import Image, ImageDraw, ImageFont
from random import choice

import numpy

from setup import setup
from utils import (
    resolve_glyphs,
    resolve_color
)

ARGS = setup("glyphs")

# Create canvas
data = numpy.zeros(
    (
        ARGS["image_height"],
        ARGS["image_width"], 
        3
    ),
    dtype=numpy.uint8
)
data[:][:] = resolve_color(ARGS["background_color"])
image = Image.fromarray(data)

def random_color(): 
    return RGB[choice(tuple(RGB.keys()))]

# Check font
draw = ImageDraw.Draw(image)
draw.fontmode = "1" if ARGS["font_aliasing"] else "0"

font = None
try:
    font = ImageFont.truetype(ARGS["font_name"], ARGS["font_size"])
except OSError:
    print(f"Font '{ARGS["font_name"]}' doesn't found, aborting")
    exit(0)

# Draw glyphs
for x in range(
        ARGS["font_margin"],
        ARGS["image_width"],
        ARGS["font_size"] + ARGS["font_margin"]
    ):
    for y in range(
            ARGS["font_margin"],
            ARGS["image_height"],
            ARGS["font_size"] + ARGS["font_margin"]
        ):
        draw.text(
            xy=(x, y),
            text=choice(resolve_glyphs(ARGS["glyph_set"])),
            font=font,
            fill=random_color()
        )

image = image.resize(
    size=(
        ARGS["image_width"] * ARGS["image_scale_factor"],
        ARGS["image_height"] * ARGS["image_scale_factor"]
    ),
    resample=Image.Resampling.BOX
)

image.save('image.png')
image.show()
