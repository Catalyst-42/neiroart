import numpy as np
from PIL import Image

from random import choice

from setup import setup
from utils import (
    resize,
    limit,
    show_and_save,
)

ARGS = setup('mapper')
samples = 'img/tilesets'

# Load and split tileset
t = np.array(Image.open(ARGS['tileset']).convert('RGB'))
tile_width, tile_height, _ = np.array(t.shape) // 4
tile_padding = ARGS['tile_padding']

# Full tile width and height
cell_width = tile_width + tile_padding
cell_height = tile_height + tile_padding

tileset = tuple(  # Slice tileset to list
    t[x:x+tile_width, y:y+tile_height]
    for x in range(0, t.shape[0], tile_width)
    for y in range(0, t.shape[1], tile_height)
)

if ARGS['as'] == 'tiles':
    ARGS['image_width'] *= cell_width 
    ARGS['image_width'] += tile_padding

    ARGS['image_height'] *= cell_height
    ARGS['image_height'] += tile_padding

# Create canvas
data = np.full(
    (ARGS['image_height'], ARGS['image_width'], 3),
    ARGS['background_color'],
    np.uint8
)

def draw_cell(canvas, x, y, tile, color):
    mask = np.all(tile == (0, 0, 0), axis=-1)
    new_tile = np.full_like(tile, ARGS['background_color'])
    new_tile[~mask] = color  # Fill non zero values with selected color

    canvas[y:y+tile.shape[0], x:x+tile.shape[1]] = new_tile

# Debug: draw tileset by tiles
if ARGS['show_tiles']:
    x = y = tile_padding
    for tile in range(16):
        color = [255] * 3
        data[y, x] = (255, 0, 0)  # Mark center
        draw_cell(data, x, y, tileset[tile], color)

        if (tile + 1) % 4 == 0:  # Go on next line
            x -= (cell_width) * 3
            y += cell_height
        else:
            x += cell_width

# Process growth
processed = dict()  # (x, y): tile_index
to_process = [(  # (x, y) values
    (ARGS['image_width'] - tile_width) // 2,
    (ARGS['image_height'] - tile_height) // 2
)]

up    = 0b1000
down  = 0b0100
left  = 0b0010
right = 0b0001

# x_vel, y_vel, dir, -dir
directions = (
    (0, -1, up, down),
    (0, 1, down, up),
    (-1, 0, left, right),
    (1, 0, right, left)
)

while to_process:
    x, y = to_process.pop(0)
    available_tiles = [*range(1, 16)] if len(processed) else [15]

    # Check available growth directions
    for direction in directions:
        check_x = x + direction[0] * cell_width
        check_y = y + direction[1] * cell_height
        front = direction[2]
        backwards = direction[3]

        in_bounds = (
            0 <= check_x <= ARGS['image_width'] - cell_width and
            0 <= check_y <= ARGS['image_height'] - cell_height
        )

        if (check_x, check_y) in processed:
            if processed[(check_x, check_y)] & backwards:
                available_tiles = [
                    tile for tile in available_tiles
                    if tile & front
                ]
            else:
                available_tiles = [
                    tile for tile in available_tiles
                    if not tile & front
                ]

        # Limit generation
        elif (
            ARGS['tile_limit'] and len(processed) > ARGS['tile_limit']
            or not in_bounds
        ):
            available_tiles = [
                tile for tile in available_tiles
                if not tile & front
            ]

    # Draw selected tile
    tile = choice(available_tiles)
    processed[(x, y)] = tile

    # Create new outgrowths
    for direction in directions:

        check_x = x + direction[0] * cell_width
        check_y = y + direction[1] * cell_height
        new_pos = (check_x, check_y)

        if not direction[2] & tile:
            continue

        if not 0 <= check_x <= ARGS['image_width'] - cell_width \
        or not 0 <= check_y <= ARGS['image_height'] - cell_height:
            continue

        if new_pos not in processed and new_pos not in to_process:
            to_process.append(new_pos)

# Paint each cell in the end
for i, pos in enumerate(processed):
    x, y = pos
    tile = processed[pos]

    progress = i / len(processed)
    color = choice(ARGS['colorset'])

    match ARGS['color_style']:
        case ':pulse':
            color = [
                limit(int(c * (1 - progress)), 0, 255) for c in color
            ]

        case ':spot':
            value = int(len(ARGS['colorset']) * progress)
            color = ARGS['colorset'][
                limit(value, 0, len(ARGS['colorset']) - 1)
            ]

    draw_cell(data, x, y, tileset[tile], color)

image = Image.fromarray(data)
image = resize(
    image,
    ARGS['image_width'] * ARGS['image_scale_factor'],
    ARGS['image_height'] * ARGS['image_scale_factor']
)

show_and_save(image, ARGS['output'], ARGS['quiet'])
