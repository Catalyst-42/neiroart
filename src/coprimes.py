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

ARGS = setup('worm')

ARGS['image_width'] = 23
ARGS['image_height'] = 13

ARGS['line_length'] = 5
ARGS['line_color'] = BLACK

BACKGROUND_COLOR = WHITE

COLOR_A = RGB['purple']
COLOR_B = RGB['yellow']

EXCLUDE_CIRCLES = False  # The o figure
EXCLUDE_CROSSES = False  # The x figure
RESIZE_TO = (ARGS['image_width']*ARGS['line_length'] * 2, ARGS['image_height']*ARGS['line_length'] * 2)

# Check WIDTH and HEIGHT
def gcd(x, y):
    while True:
        if x != 0 and y != 0:
            (x := x % y) if x > y else (y := y % x)
        else:
            return x + y

if gcd(ARGS['image_width'], ARGS['image_height']) != 1:
    print(f"{ARGS['image_width']} and {ARGS['image_height']} isn't coprime numbers!")
    exit()

data = np.zeros((ARGS['image_height']*ARGS['line_length'], ARGS['image_width']*ARGS['line_length'], 3), dtype=np.uint8)
data[:][:] = BACKGROUND_COLOR

x, y = 0, 0
iters = 0
x_vel = ARGS['line_length']
y_vel = ARGS['line_length']

# Create pattern on field
while True:
    # Draw line or pixel
    if iters % 2 == 0:
        for i in range(ARGS['line_length']):
            if x_vel == y_vel:
                data[y + i][x + i] = ARGS['line_color']
            else:
                data[y - i + ARGS['line_length']-1][x + i] = ARGS['line_color']
    
    # Move on next tile
    x += x_vel
    y += y_vel

    # Check directons
    swaps = 0
    if x >= ARGS['image_width']*ARGS['line_length'] or x <= -1:
        swaps += 1
        x -= x_vel
        x_vel = -x_vel

    if y >= ARGS['image_height']*ARGS['line_length'] or y <= -1:
        swaps += 1
        y -= y_vel
        y_vel = -y_vel

    # Wnd drawing in corner
    if swaps == 2:
        break

    iters += 1

print(f'Generation done ({iters})')

# Finds and exludes small figures on image
def make_custom_figure(figure_width, figure_height, *data):
    # Here you can make own figure samples
    # data = ((x, y, y_vel), (x, y, y_vel), ...)

    figure = np.zeros((figure_width*ARGS['line_length'], figure_height*ARGS['line_length'], 3), dtype=np.uint8)
    figure[:][:] = BACKGROUND_COLOR
    
    for x, y, y_vel in data:
        for i in range(ARGS['line_length']):
            if y_vel == 1:
                figure[y*ARGS['line_length'] + i][x*ARGS['line_length'] + i] = ARGS['line_color']
            else:
                figure[y*ARGS['line_length'] - i + ARGS['line_length']-1][x*ARGS['line_length'] + i] = ARGS['line_color']

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
                    data[y*ARGS['line_length'] + cy][x*ARGS['line_length'] + cx] = BACKGROUND_COLOR

if EXCLUDE_CIRCLES:
    circle = make_custom_figure(2, 2, (0, 0, -1), (1, 0, 1), (0, 1, 1), (1, 1, -1))
    exclude_figure(circle, 2, 2)
    print("Circles excluded")

if EXCLUDE_CROSSES:
    cross = make_custom_figure(4, 4, (0, 0, -1), (1, 0, 1), (2, 0, -1), (3, 0, 1), (0, 1, 1), (3, 1, -1), (0, 2, -1), (3, 2, 1), (0, 3, 1), (1, 3, -1), (2, 3, 1), (3, 3, -1))
    exclude_figure(cross, 4, 4)
    print("Crosses excluded")

# Paint
x_vel = 1
y_vel = 0

x = 0
y = 0
iters = 0

for y in range(ARGS['image_height'] * ARGS['line_length']):
    color_a = COLOR_A
    color_b = COLOR_B

    if y % (4*ARGS['line_length']) >= 2*ARGS['line_length']:
        color_a, color_b = color_b, color_a 

    for x in range(ARGS['image_width'] * ARGS['line_length']):
        if all(data[y][x][:] == ARGS['line_color']):
            color_a, color_b = color_b, color_a
        else:
            data[y][x] = color_a

print("Coloring done")

image = Image.fromarray(data)
image = image.resize(RESIZE_TO, resample=Image.Resampling.BOX)

image.save('image.png')
image.show()
