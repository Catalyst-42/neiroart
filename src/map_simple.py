from random import choice, randint
from colors import RGB, BLACK, WHITE
from PIL import Image

import numpy

WIDTH = 256
HEIGHT = 256

COLORS = (WHITE, )
BACKGROUND_COLOR = BLACK

STEP_LENGTH_MIN = 1
STEP_LENGTH_MAX = 1

MAX_ITERS = 8192
RESIZE_TO = (WIDTH*2, HEIGHT*2)

data = numpy.zeros((WIDTH, HEIGHT, 3), dtype=numpy.uint8)
data[:][:] = BACKGROUND_COLOR

x, y = WIDTH//2, HEIGHT//2
direction = choice((1, 2, 3, 4))
iters = 0

# random walk
for i in range(MAX_ITERS):
    # set move directoin (can't move backwards)
    if direction == 1: direction = choice((3, 4))
    elif direction == 2: direction = choice((3, 4))
    elif direction == 3: direction = choice((1, 2))
    elif direction == 4: direction = choice((1, 2))
    
    # make n steps in one direction
    for step in range(randint(STEP_LENGTH_MIN, STEP_LENGTH_MAX)):
        # set layer color
        if all(data[x][y][:] == BACKGROUND_COLOR): # background layer
            data[x][y] = COLORS[0]
        else:
            for color in range(len(COLORS) - 1): # layers above COLORS[0]
                if all(data[x][y][:] == COLORS[color]):
                    data[x][y] = COLORS[color + 1]
                    break
        
        # move in direction
        match direction:
            case 1: y+=1 # up
            case 2: y-=1 # down
            case 3: x+=1 # right
            case 4: x-=1 # left
        
        # normalize x and y (map is tor)
        if x >= WIDTH: x-=WIDTH
        if x < 0: x+=WIDTH
        if y >= HEIGHT: y-=HEIGHT
        if y < 0: y+=HEIGHT

        iters += 1

print(f'Generation done ({iters})')

image = Image.fromarray(data)
image = image.transpose(Image.Transpose.ROTATE_90)
image = image.resize(RESIZE_TO, resample=Image.Resampling.BOX)

image.save('image.png')
image.show()
