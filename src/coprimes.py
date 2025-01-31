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


def draw_line(canvas, x, y, x_vel, y_vel):
    l = ARGS['line_length']
    t = ARGS['line_thickness']

    for i in range(l):
        canvas[y + i*y_vel][x + i*x_vel] = ARGS['line_color']

        for j in range(1, t):
            dx, dy = i * x_vel, i * y_vel
            directions = {
                1: j < l - i,
                -1: j <= i
            }

            for d in directions:
                if directions[y_vel * d]:
                    canvas[y + dy + j*d][x + dx] = ARGS['line_color']


# Create carpet
while bounces != 2:
    bounces = 0

    # Draw line or pixel
    if step % 2 == 0:
        draw_line(data, x, y, x_vel, y_vel)

    # Move on next tile
    x += x_vel * l
    y += y_vel * l

    # Bounce
    if not -1 < x < ARGS['image_width'] * l:
        x -= x_vel
        x_vel = -x_vel
        bounces += 1

    if not -1 < y < ARGS['image_height'] * l:
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
        x, y = x*l, y*l

        if y_vel == -1:
            y += l - 1

        draw_line(figure, x, y, 1, y_vel)

    # Show sample
    # image = Image.fromarray(figure)
    # image.show()

    # Compare and remove figure samples in sliding window
    for y in range(ARGS['image_height'] - (h-1)):
        for x in range(ARGS['image_width'] - (w-1)):
            window = np.s_[y*l:(y+h)*l, x*l:(x+w)*l]

            if np.all(data[window] == figure):
                data[window] = ARGS['background_color_a']


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
            on_baseline = any((
                (x % (2*l) == y % (2*l)),
                ((x+1) % (2*l) == -y % (2*l))
            ))

            if on_baseline and np.all(data[y][x] == ARGS['line_color']):
                color_a, color_b = color_b, color_a
            
            if not np.all(data[y][x] == ARGS['line_color']):
                data[y][x] = color_a

            # Show baseline
            # if on_baseline:
            #     data[y][x] = (255, 0,0)

image = Image.fromarray(data)
image = resize(
    image,
    ARGS['image_width']*l * ARGS['image_scale_factor'],
    ARGS['image_height']*l * ARGS['image_scale_factor'],
)

show_and_save(image, ARGS['output'], ARGS['quiet'])
