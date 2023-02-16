from random import choice, randint

import numpy
from PIL import Image

MAX_X = 256
MAX_Y = 256
MAX_ITERS = 1024
RESIZE_TO = (512, 512)

colors_RGB = {
    'red': (255, 99, 132),
    'orange': (255, 159, 64),
    'yellow': (255, 205, 86),
    'green': (75, 192, 192),
    'blue': (54, 162, 235),
    'purple': (153, 102, 255),
    'grey': (201, 203, 207),
    'bg': (21, 23, 32)}
color_names = (
    'red',
    'orange',
    'purple')

data = numpy.zeros((MAX_X, MAX_Y, 3), dtype=numpy.uint8)
data[:][:] = colors_RGB['bg']
color = colors_RGB['blue']

def randcolor(): return colors_RGB[choice(color_names)]

def draw_side(x, y, side):
    global color
    if randint(1, 100) == 1:
        color = randcolor()

    def right_enter(): data[x:x+3, y] = color # right
    def left_enter(): data[x-2:x+1, y] = color # left
    def up_enter(): data[x, y:y+3] = color # up
    def down_enter(): data[x, y-2:y+1] = color # down

    if side in (1, 2, 4, 8, 11, 12, 13, 15): 
        right_enter()
        if data[x+6, y][0] == 21 and (x+6, y) not in working_stack: working_stack.append((x+6, y))
    if side in (1, 2, 6, 9, 10, 13, 14, 15): 
        left_enter()
        if data[x-6, y][0] == 21 and (x-6, y) not in working_stack: working_stack.append((x-6, y))
    if side in (1, 3, 5, 8, 9, 12, 13, 14): 
        up_enter()
        if data[x, y+6][0] == 21 and (x, y+6) not in working_stack: working_stack.append((x, y+6))
    if side in (1, 3, 7, 10, 11, 12, 14, 15): 
        down_enter()
        if data[x, y-6][0] == 21 and (x, y-6) not in working_stack: working_stack.append((x, y-6))

# Проверка всех ячеек draw_side
# x, y = 20, 44
# working_stack = []
# for side in range(16):
#     x += 6
#     if (side) % 4 == 0: 
#         x = 20
#         y -= 6
#     draw_side(x, y, side)
# data[x, y] = colors_RGB['red']

x, y = MAX_X//2, MAX_Y//2
working_stack = []
iters = 0

draw_side(x, y, choice((1, 12, 13, 14, 15)))

while len(working_stack):
    iters += 1
    x, y = working_stack.pop(randint(0, len(working_stack)-1))
    choice_side = [_ for _ in range(1, 16)]

    # right
    if data[x+6, y][0] != 21 and data[x+4, y][0] == 21:
        for _ in (1, 2, 4, 8, 11, 12, 13, 15):
            if _ in choice_side: choice_side.remove(_)
    elif data[x+6, y][0] != 21 and data[x+4, y][0] != 21:
        for _ in (0, 3, 5, 6, 7, 9, 10, 14):
            if _ in choice_side: choice_side.remove(_)

    # left
    if data[x-6, y][0] != 21 and data[x-4, y][0] == 21:
        for _ in (1, 2, 6, 9, 10, 13, 14, 15):
            if _ in choice_side: choice_side.remove(_)
    elif data[x-6, y][0] != 21 and data[x-4, y][0] != 21:
        for _ in (0, 3, 4, 5, 7, 8, 11, 12):
            if _ in choice_side: choice_side.remove(_)

    #  up
    if data[x, y+6][0] != 21 and data[x, y+4][0] == 21:
        for _ in (1, 3, 5, 8, 9, 12, 13, 14):
            if _ in choice_side: choice_side.remove(_)
    elif data[x, y+6][0] != 21 and data[x, y+4][0] != 21:
        for _ in (0, 2, 4, 6, 7, 10, 11, 15):
            if _ in choice_side: choice_side.remove(_)

    # down
    if data[x, y-6][0] != 21 and data[x, y-4][0] == 21:
        for _ in (1, 3, 7, 10, 11, 12, 14, 15):
            if _ in choice_side: choice_side.remove(_)
    elif data[x, y-6][0] != 21 and data[x, y-4][0] != 21:
        for _ in (0, 2, 4, 5, 6, 8, 9, 13):
            if _ in choice_side: choice_side.remove(_)

    # more straight path
    # if 2 in choice_side: choice_side.append(2); choice_side.append(2); choice_side.append(2)
    # if 2 in choice_side: choice_side.append(2); choice_side.append(2); choice_side.append(2)

    if not 12<x<(MAX_X-12) or not 12<y<(MAX_Y-12) or iters > MAX_ITERS:
        for _ in range(4, 8):
            if _ in choice_side: choice_side = [_]

    # print(choice_side)
    side = choice(choice_side)
    draw_side(x, y, side)

print(f'iters: {iters}')

image = Image.fromarray(data)
image = image.transpose(Image.Transpose.ROTATE_90)
image = image.resize(RESIZE_TO, resample=Image.Resampling.BOX)
image.save('image.png')
image.show()
