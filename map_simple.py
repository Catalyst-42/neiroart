from random import choice, randint

import numpy
from PIL import Image

MAX_X = 256
MAX_Y = 256
MAX_ITERS = 4096
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
    'yellow',
    'green',
    'blue',
    'purple',
    'grey')

data = numpy.zeros((MAX_X, MAX_Y, 3), dtype=numpy.uint8)
data[:][:] = colors_RGB['bg']

# def randcolor(): return colors_RGB[choice(color_names)]

def normalaize():
    global x, y
    if x >= MAX_X: x-=MAX_X
    if x < 0: x+=MAX_X
    if y >= MAX_Y: y-=MAX_Y
    if y < 0: y+=MAX_Y

x, y = MAX_X//2, MAX_Y//2
direction = 1
for i in range(MAX_ITERS):
    # 1 2 3 4 = up down rigth left
    if direction == 1: direction = choice((3, 4))
    elif direction == 2: direction = choice((3, 4))
    elif direction == 3: direction = choice((1, 2))
    elif direction == 4: direction = choice((1, 2))
    
    match direction:
        case 1:
            for _ in range(randint(2, 8)):
                if all(data[x][y][:] == colors_RGB['bg']): data[x][y] = colors_RGB['purple']
                elif all(data[x][y][:] == colors_RGB['purple']): data[x][y] = colors_RGB['blue']
                else: data[x][y] = colors_RGB['green']
                y+=1 # randint(1, 8)
                normalaize()
        case 2:
            for _ in range(randint(2, 8)):
                if all(data[x][y][:] == colors_RGB['bg']): data[x][y] = colors_RGB['purple']
                elif all(data[x][y][:] == colors_RGB['purple']): data[x][y] = colors_RGB['blue']
                else: data[x][y] = colors_RGB['green']
                y-=1 # randint(1, 8)
                normalaize()
        case 3:
            for _ in range(randint(2, 8)):
                if all(data[x][y][:] == colors_RGB['bg']): data[x][y] = colors_RGB['purple']
                elif all(data[x][y][:] == colors_RGB['purple']): data[x][y] = colors_RGB['blue']
                else: data[x][y] = colors_RGB['green']
                x+=1 # randint(1, 8)
                normalaize()
        case 4:
            for _ in range(randint(2, 8)):
                if all(data[x][y][:] == colors_RGB['bg']): data[x][y] = colors_RGB['purple']
                elif all(data[x][y][:] == colors_RGB['purple']): data[x][y] = colors_RGB['blue']
                else: data[x][y] = colors_RGB['green']
                x-=1 # randint(1, 8)
                normalaize()

image = Image.fromarray(data)
image = image.transpose(Image.Transpose.ROTATE_90)
image = image.resize(RESIZE_TO, resample=Image.Resampling.BOX)
image.save('image.png')
image.show()
