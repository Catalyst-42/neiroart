import numpy as np
from PIL import (
    Image,
    ImageDraw,
    ImageFont
)

from random import choice

from setup import setup
from utils import (
    resolve_glyphs,
    resolve_colors,
    resolve_color
)

ARGS = setup("glyphs")

# Create canvas
image = Image.fromarray(np.full(
    (ARGS["image_height"], ARGS["image_width"], 3),
    resolve_color(ARGS["background_color"]),
    np.uint8
))

colors = resolve_colors(ARGS["glyph_color_set"])
glyphs = resolve_glyphs(ARGS["glyph_set"])

# Setup font
font = None
draw = ImageDraw.Draw(image)
draw.fontmode = "1" if ARGS["font_aliasing"] else "0"

try:
    font = ImageFont.truetype(
        ARGS["font_name"],
        ARGS["font_size"]
    )
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
            text=choice(glyphs),
            font=font,
            fill=choice(colors)
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
