from random import choice, randint
from colors import RGB, BLACK
from PIL import Image

import numpy

WIDTH = 256
HEIGHT = 256

COLOR = RGB['purple']
SWITCH_COLORS = [RGB[color] for color in RGB.keys()] # all colors
BACKGROUND_COLOR = BLACK

MAX_ITERS = 512
RESIZE_TO = (WIDTH*2, HEIGHT*2)

data = numpy.zeros((WIDTH, HEIGHT, 3), dtype=numpy.uint8)
data[:][:] = BACKGROUND_COLOR

def draw_side(x, y, side):
    global COLOR

    # change color in 1% change
    if randint(1, 100) == 42:
        COLOR = choice(SWITCH_COLORS)

    # draw tile
    def right(): data[x+2, y-2:y+3] = COLOR
    def left(): data[x-2, y-2:y+3] = COLOR
    def up(): data[x-2:x+3, y+2] = COLOR
    def down(): data[x-2:x+3, y-2] = COLOR

    def right_enter(): data[x+2, y-2:y] = data[x+2, y+1:y+3] = COLOR
    def left_enter(): data[x-2, y-2:y] = data[x-2, y+1:y+3] = COLOR
    def up_enter(): data[x-2:x, y+2] = data[x+1:x+3, y+2] = COLOR
    def down_enter(): data[x-2:x, y-2] = data[x+1:x+3, y-2] = COLOR
    
    if side in (0, 3, 5, 6, 7, 9, 10, 14): right()
    if side in (0, 3, 4, 5, 7, 8, 11, 12): left()
    if side in (0, 2, 4, 6, 7, 10, 11, 15): up()
    if side in (0, 2, 4, 5, 6, 8, 9, 13): down()

    if side in (1, 2, 4, 8, 11, 12, 13, 15):
        right_enter()
        if all(data[x+4, y-1][:] == BACKGROUND_COLOR) and (x+6, y) not in working_stack:
            working_stack.append((x+6, y))
    if side in (1, 2, 6, 9, 10, 13, 14, 15):
        left_enter()
        if all(data[x-4, y-1][:] == BACKGROUND_COLOR) and (x-6, y) not in working_stack:
            working_stack.append((x-6, y))
    if side in (1, 3, 5, 8, 9, 12, 13, 14):
        up_enter()
        if all(data[x-1, y+4][:] == BACKGROUND_COLOR) and (x, y+6) not in working_stack:
            working_stack.append((x, y+6))
    if side in (1, 3, 7, 10, 11, 12, 14, 15):
        down_enter()
        if all(data[x-1, y-4][:] == BACKGROUND_COLOR) and (x, y-6) not in working_stack:
            working_stack.append((x, y-6))

# debug: draw all tile samples
# x, y = 20, 44
# working_stack = []
# for side in range(16):
#     x += 6
#     if (side) % 4 == 0: 
#         x = 20
#         y -= 6
#     draw_side(x, y, side)
#     data[x, y] = RGB['red']

x, y = WIDTH//2, HEIGHT//2
working_stack = []
iters = 0

# draw first tile
draw_side(x, y, choice((1, 12, 13, 14, 15)))

# generate tiles
while len(working_stack):
    x, y = working_stack.pop(randint(0, len(working_stack)-1))
    sides = [side for side in range(1, 16)]

    # exclude unavailable sides to expanding
    def remove_sides(*sides_to_remove):
        for side in sides_to_remove:
            if side in sides: sides.remove(side)

    # right
    if all(data[x+4, y-1][:] != BACKGROUND_COLOR) and all(data[x+4, y][:] != BACKGROUND_COLOR):
        remove_sides(1, 2, 4, 8, 11, 12, 13, 15)
    elif all(data[x+4, y-1][:] != BACKGROUND_COLOR) and all(data[x+4, y][:] == BACKGROUND_COLOR):
        remove_sides(0, 3, 5, 6, 7, 9, 10, 14)

    # left
    if all(data[x-4, y-1][:] != BACKGROUND_COLOR) and all(data[x-4, y][:] != BACKGROUND_COLOR):
        remove_sides(1, 2, 6, 9, 10, 13, 14, 15)
    elif all(data[x-4, y-1][:] != BACKGROUND_COLOR) and all(data[x-4, y][:] == BACKGROUND_COLOR):
        remove_sides(0, 3, 4, 5, 7, 8, 11, 12)

    #  up
    if all(data[x-1, y+4][:] != BACKGROUND_COLOR) and all(data[x, y+4][:] != BACKGROUND_COLOR):
        remove_sides(1, 3, 5, 8, 9, 12, 13, 14)
    elif all(data[x-1, y+4][:] != BACKGROUND_COLOR) and all(data[x, y+4][:] == BACKGROUND_COLOR):
        remove_sides(0, 2, 4, 6, 7, 10, 11, 15)

    # down
    if all(data[x-1, y-4][:] != BACKGROUND_COLOR) and all(data[x, y-4][:] != BACKGROUND_COLOR):
        remove_sides(1, 3, 7, 10, 11, 12, 14, 15)
    elif all(data[x-1, y-4][:] != BACKGROUND_COLOR) and all(data[x, y-4][:] == BACKGROUND_COLOR):
        remove_sides(0, 2, 4, 5, 6, 8, 9, 13)

    # add more straight paths (better on huge maps)
    # if 2 in sides: sides.append(2); sides.append(2); sides.append(2)
    # if 3 in sides: sides.append(3); sides.append(3); sides.append(3)

    # make dead ends
    if not 12<x<(WIDTH-12) or not 12<y<(HEIGHT-12) or iters > MAX_ITERS: 
        for side in range(4, 8):
            if side in sides: sides = [side]

    # choice available side and draw it
    side = choice(sides)
    draw_side(x, y, side)

    iters += 1

print(f'Generation done ({iters})')

image = Image.fromarray(data)
image = image.transpose(Image.Transpose.ROTATE_90)
image = image.resize(RESIZE_TO, resample=Image.Resampling.BOX)

image.save('image.png')
image.show()
