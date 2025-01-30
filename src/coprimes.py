from PIL import Image
import numpy as np

from math import gcd
from random import randint

from setup import setup
from groups import figures
from utils import (
    resize,
    show_and_save,
)

# Original idea gathered from Foo52
# https://www.youtube.com/watch?v=IdwR58QmCo8
ARGS = setup('coprimes')
l = ARGS['line_length']

width = ARGS['image_width']
height = ARGS['image_height']


def get_coprimes(iw=None, ih=None):
    while True:
        width = randint(10, 100) if iw is None else width
        height = randint(10, 100) if ih is None else height

        if gcd(width, height) == 1:
            return width, height


if width is None and height is not None:
    width, height = get_coprimes(width, height)

elif width is None and height is not None:
    width, height = get_coprimes(width, height)

elif width is None and height is None or gcd(width, height) != 1:
    ARGS['image_width'], ARGS['image_height'] = get_coprimes()

# Create canvas
data = np.full((
        ARGS['image_height'] * l,
        ARGS['image_width'] * l,
        3
    ),
    ARGS['background_color_a'],
    np.uint8
)

x, y = 0, 0
x_vel, y_vel = 1, 1

step = 0
bounces = 0

# Create carpet
while bounces != 2:
    bounces = 0

    # Draw line or pixel
    if step % 2 == 0:
        for i in range(l):
            data[y + i*y_vel][x + i*x_vel] = ARGS['line_color']

    # Move on next tile
    x += x_vel * l
    y += y_vel * l

    # Bounce
    if not 0 < x < ARGS['image_width'] * l:
        # if ARGS['line_length'] > 1:
        x -= x_vel
        x_vel = -x_vel
        bounces += 1

    if not 0 < y < ARGS['image_height'] * l:
        # if ARGS['line_length'] > 1:
        y -= y_vel
        y_vel = -y_vel
        bounces += 1

    step += 1


def exclude_figure(figure):
    w, h, cells = figure.values()

    figure = np.full(
        (w * l, h * l, 3),
        ARGS['background_color_a'],
        np.uint8
    )

    # Generate figure
    for x, y, y_vel in cells:            
        for i in range(l):
            xi = x*l + i
            yi = y*l + i

            if y_vel != 1:
                yi += l - 1 - 2*i

            figure[yi][xi] = ARGS['line_color']

    # Show sample
    # image = Image.fromarray(figure)
    # image.show()

    # Search and exclude figure from canvas
    for y in range(ARGS['image_height'] - (h-1)):
        for x in range(ARGS['image_width'] - (w-1)):
            is_figure = True

            # Compare sample to figure sample
            for cy in range(l * h):
                for cx in range(l * w):
                    if any(
                        data[y*l + cy][x*l + cx][:] != figure[cy][cx][:]
                    ):
                        is_figure = False
                        break

            # Remove figure
            if not is_figure:
                continue

            for cy in range(l * h):
                for cx in range(l * w):
                    data[y*l + cy][x*l + cx] = ARGS['background_color_a']


for figure in ARGS['exclude']:
    exclude_figure(figures[figure])

# Paint
x, y = 0, 0

if ARGS['background_color_a'] != ARGS['background_color_b']:
    for y in range(ARGS['image_height'] * l):
        color_a = ARGS['background_color_a']
        color_b = ARGS['background_color_b']

        if y % (4 * l) >= 2 * l:
            color_a, color_b = color_b, color_a 

        for x in range(ARGS['image_width'] * l):
            if all(data[y][x][:] == ARGS['line_color']):
                color_a, color_b = color_b, color_a
            else:
                data[y][x] = color_a

image = Image.fromarray(data)
image = resize(
    image,
    ARGS['image_width']*l * ARGS['image_scale_factor'],
    ARGS['image_height']*l * ARGS['image_scale_factor'],
)

show_and_save(image, ARGS['output'], ARGS['quiet'])
