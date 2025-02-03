import numpy as np
from PIL import Image

from random import (
    choice,
    randint
)

from setup import setup
from utils import (
    resize,
    show_and_save
)

ARGS = setup('worm')

# Create canvas
data = np.full(
    (ARGS['image_height'], ARGS['image_width'], 3),
    ARGS['background_color'],
    np.uint8
)

directions = []
cells = dict()  # (x, y): visits

if ARGS['move_straight']:
    directions.extend((
        (0, -1),  # Up
        (0, 1),   # Down
        (-1, 0),  # Left
        (1, 0),   # Right
    ))

if ARGS['move_diagonal']:
    directions.extend((
        (-1, -1),  # Up left
        (-1, 1),   # Up right
        (1, -1),   # Down left
        (1, 1),    # Down right
    ))

# Random walk
x, y = ARGS['image_width']//2, ARGS['image_height']//2
direction = choice(directions)

for i in range(ARGS['step_limit']):
    # Choice direction
    available_directions = directions.copy()
    if not ARGS['move_backwards']:  # Remove previous direction
        available_directions.remove(direction)
    direction = choice(available_directions)

    # Make steps in this direction
    for step in range(
        randint(ARGS['step_min_length'], ARGS['step_max_length'])
    ):
        x += direction[0]
        y += direction[1]

        if not 0 <= x <= ARGS['image_width'] - 1:
            x = abs(x - ARGS['image_width'] + 2)

        if not 0 <= y <= ARGS['image_height'] - 1:
            y = abs(y - ARGS['image_height'] + 2)
        
        cells.setdefault((x, y), 1)
        cells[(x, y)] += 1

# Paint
for i, cell in enumerate(cells):
    color = min(cells[cell], len(ARGS['colorset'])) - 1
    x, y = cell

    data[y][x] = ARGS['colorset'][color]

image = Image.fromarray(data)
image = resize(
    image,
    ARGS['image_width'] * ARGS['image_scale_factor'],
    ARGS['image_height'] * ARGS['image_scale_factor']
)

show_and_save(image, ARGS['output'], ARGS['quiet'])
