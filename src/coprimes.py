from PIL import Image
import numpy as np

from colors import RGB, BLACK, WHITE

from setup import setup
from utils import (
    resize,
    show_and_save,
)

# Original idea: https://www.youtube.com/watch?v=IdwR58QmCo8

# WIDTH and HEIGHT must be coprime numbers
# (different prime numbers alaways coprime)

ARGS = setup('coprimes')

# Check WIDTH and HEIGHT
def gcd(x, y):
    while True:
        if x != 0 and y != 0:
            (x := x % y) if x > y else (y := y % x)
        else:
            return x + y

if gcd(ARGS['image_width'], ARGS['image_height']) != 1:
    print(
        f"{ARGS['image_width']} and {ARGS['image_height']} isn't coprime numbers!")
    exit()

# Create canvas
data = np.full((
        ARGS['image_height'] * ARGS['line_length'],
        ARGS['image_width'] * ARGS['line_length'],
        3
    ),
    ARGS['background_color_a'],
    np.uint8
)

x, y = 0, 0
step = 0

x_vel = 1
y_vel = 1

bounces = 0

# Create pattern on field
while bounces != 2:
    bounces = 0

    # Draw line or pixel
    if step % 2 == 0:
        for i in range(ARGS['line_length']):
            data[y + i*y_vel][x + i*x_vel] = ARGS['line_color']
    
    # Move on next tile
    x += x_vel * ARGS['line_length']
    y += y_vel * ARGS['line_length']

    # Bounce
    if not 0 < x < ARGS['image_width'] * ARGS['line_length']:
        x_vel = -x_vel
        x += x_vel
        bounces += 1

    if not 0 < y < ARGS['image_height'] * ARGS['line_length']:
        y -= y_vel
        y_vel = -y_vel
        bounces += 1

    step += 1

# Finds and exludes small figures on image
def make_custom_figure(figure_width, figure_height, *data):
    # Here you can make own figure samples
    # data = ((x, y, y_vel), (x, y, y_vel), ...)
    figure = np.full((
            figure_width * ARGS['line_length'],
            figure_height * ARGS['line_length'],
            3
        ),
        ARGS['background_color_a'],
        np.uint8
    )

    for x, y, y_vel in data:            
        for i in range(ARGS['line_length']):
            xi = x*ARGS['line_length'] + i
            yi = y*ARGS['line_length'] + i

            if y_vel != 1:
                yi += ARGS['line_length'] - 1 - 2*i
            
            figure[yi][xi] = ARGS['line_color']

    # Show sample
    # image = Image.fromarray(figure)
    # image.show()

    return figure

def exclude_figure(figure, figure_width, figure_height):
    for y in range(ARGS['image_height'] - (figure_height-1)):
        for x in range(ARGS['image_width'] - (figure_width-1)):
            is_figure = True

            # Compare sample to figure sample
            for cy in range(ARGS['line_length'] * figure_height):
                for cx in range(ARGS['line_length'] * figure_width):
                    if any(data[y*ARGS['line_length'] + cy][x*ARGS['line_length'] + cx][:] != figure[cy][cx][:]):
                        is_figure = False
                        break

            # Remove figure
            if not is_figure:
                continue

            for cy in range(ARGS['line_length'] * figure_height):
                for cx in range(ARGS['line_length'] * figure_width):
                    data[y*ARGS['line_length'] + cy][x*ARGS['line_length'] + cx] = ARGS['background_color_a']

if ARGS['exclude_circles']:
    circle = make_custom_figure(2, 2, (0, 0, -1), (1, 0, 1), (0, 1, 1), (1, 1, -1))
    exclude_figure(circle, 2, 2)
    print("Circles excluded")

if ARGS['exclude_crosses']:
    cross = make_custom_figure(4, 4, (0, 0, -1), (1, 0, 1), (2, 0, -1), (3, 0, 1), (0, 1, 1), (3, 1, -1), (0, 2, -1), (3, 2, 1), (0, 3, 1), (1, 3, -1), (2, 3, 1), (3, 3, -1))
    exclude_figure(cross, 4, 4)
    print("Crosses excluded")

# Paint
x_vel = 1
y_vel = 0

x = 0
y = 0
step = 0

for y in range(ARGS['image_height'] * ARGS['line_length']):
    color_a = ARGS['background_color_a']
    color_b = ARGS['background_color_b']

    if y % (4*ARGS['line_length']) >= 2*ARGS['line_length']:
        color_a, color_b = color_b, color_a 

    for x in range(ARGS['image_width'] * ARGS['line_length']):
        if all(data[y][x][:] == ARGS['line_color']):
            color_a, color_b = color_b, color_a
        else:
            data[y][x] = color_a

print("Coloring done")

image = Image.fromarray(data)
image = resize(
    image,
    ARGS['image_width']*ARGS['line_length'] * ARGS['image_scale_factor'],
    ARGS['image_height']*ARGS['line_length'] * ARGS['image_scale_factor'],
)

show_and_save(image, ARGS['output'], ARGS['quiet'])
