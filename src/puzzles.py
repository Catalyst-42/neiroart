import numpy as np
from PIL import (
    Image,
    ImageDraw
)

from math import ceil
from random import choice

from setup import setup
from utils import (
    resize,
    show_and_save
)

ARGS = setup('puzzles')
s = ARGS['tile_side']

if ARGS['by'] == 'tiles':
    ARGS['image_width'] *= (s + 1)
    ARGS['image_width'] += 1

    ARGS['image_height'] *= (s + 1)
    ARGS['image_height'] += 1

# Create canvas
data = np.full(
    (ARGS['image_height'], ARGS['image_width'], 3),
    tuple(255 - c for c in ARGS['line_color']),
    np.uint8
)

# Image border
data[0] = ARGS['line_color']
data[-1] = ARGS['line_color']

data[:, 0] = ARGS['line_color']
data[:, -1] = ARGS['line_color']

# Ledges
l = ARGS['ledge_length']
d = ARGS['ledge_depth']
v = ceil((s - l) / 2)  # Length of baseline parts

for y in range(0, ARGS['image_height'] - 1, s + 1):    
    for x in range(0, ARGS['image_width'] - 1, s + 1):
        if y != 0 and y != ARGS['image_height'] - 1:
            # _    _ of  _|‾‾|_
            data[y, x:x+v + 1] = ARGS['line_color']
            data[y, x+v+1+l:x+s+1] = ARGS['line_color']

            #   ‾‾   of  _|‾‾|_
            dy = choice((-1, 1))
            data[y+dy*d, x+v+1:x+v+1+l] = ARGS['line_color']

            #  |  |  of  _|‾‾|_
            data[y:y+dy*d+dy:dy, x+v] = ARGS['line_color']
            data[y:y+dy*d+dy:dy, x+v+1+l] = ARGS['line_color']

        # Same things but on y axis
        if x != 0 and x != ARGS['image_width'] - 1:
            data[y:y+v + 1, x] = ARGS['line_color']
            data[y+v+1+l:y+s+1, x] = ARGS['line_color']
            
            dx = choice((-1, 1))
            data[y+v+1:y+v+1+l, x+dx*d] = ARGS['line_color']

            data[y+v, x:x+dx*d+dx:dx] = ARGS['line_color']
            data[y+v+1+l, x:x+dx*d+dx:dx] = ARGS['line_color']

# Paint
image = Image.fromarray(data)

for y in range(0, ARGS['image_height'] - 1, s + 1):    
    for x in range(0, ARGS['image_width'] - 1, s + 1):
        ImageDraw.floodfill(image, (x+1, y+1), choice(ARGS['colorset']))

image = resize(
    image,
    ARGS['image_width'] * ARGS['image_scale_factor'],
    ARGS['image_height'] * ARGS['image_scale_factor'],
)

show_and_save(image, ARGS['output'], ARGS['quiet'])
