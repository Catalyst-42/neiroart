from colors import RGB, BLACK, WHITE
from PIL import Image, ImageDraw
from random import choice

from setup import inputs
import numpy

def gen():
    CONSTANTS = inputs['puzzles']
    
    # one puzzle is 8x8 pixels
    WIDTH = CONSTANTS['WIDTH'][1]
    HEIGHT = CONSTANTS['HEIGHT'][1]

    LINE_COLOR = CONSTANTS['LINE_COLOR'][1]
    BACKGROUND_COLOR = CONSTANTS['BACKGROUND_COLOR'][1]

    COLORED = CONSTANTS['COLORED'][1]  # o figure
    CELL_COLORS = CONSTANTS['CELL_COLORS'][1]  # x figure

    RESIZE_TO = CONSTANTS['RESIZE_TO'][1]
    
    data = numpy.zeros((HEIGHT, WIDTH, 3), dtype=numpy.uint8)
    data[:][:] = BACKGROUND_COLOR

    # generate puzzle pattern
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            # change puzzle ledge
            if x % 8 == 0:
                y_shift = choice((-1, 1))

            if y % 8 == 0:
                x_shift = [choice((-1, 1)) for _ in range(HEIGHT // 8)]
            
            # draw puzzle
            if y % 8 == 0 or x % 8 == 0:
                if x%8 in (3, 5) or y%8 in (3, 5):
                    data[y][x] = LINE_COLOR

                if (y == 0 or y == HEIGHT-1 or x == 0 or x == WIDTH-1):
                    data[y][x] = LINE_COLOR
                else:
                    data[y + y_shift if (2 < x%8 < 6) else y][x + x_shift[x//8] if (2 < y%8 < 6) else x][:] = LINE_COLOR

    image = Image.fromarray(data)

    # coloring each puzzle
    if COLORED:
        for y in range(0, HEIGHT, 8):
            for x in range(0, WIDTH, 8):
                ImageDraw.floodfill(image, (x+4, y+4), choice(CELL_COLORS))

    image = image.resize(RESIZE_TO, resample=Image.Resampling.BOX)

    image.save('image.png')
    image.show()
