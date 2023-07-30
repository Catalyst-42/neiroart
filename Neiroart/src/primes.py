from colors import RGB, BLACK, WHITE
from PIL import Image

import numpy

# Original idea: https://www.youtube.com/watch?v=IdwR58QmCo8

# WIDTH and HEIGHT must be coprime numbers
# (different prime numbers alaways coprime)

WIDTH = 23
HEIGHT = 13

LINE_LENGTH = 3
LINE_COLOR = BLACK

BACKGROUND_COLOR = WHITE

COLORED = True
COLOR_A = RGB['purple']
COLOR_B = RGB['yellow']

EXCLUDE_CIRCLES = False # o figure
EXCLUDE_CROSSES = False # x figure
RESIZE_TO = (WIDTH*LINE_LENGTH * 2, HEIGHT*LINE_LENGTH * 2)

# check WIDTH and HEIGHT
def gcd(x, y):
    while True:
        if x != 0 and y != 0:
            (x := x % y) if x > y else (y := y % x)
        else:
            return x+y

if gcd(WIDTH, HEIGHT) != 1:
    print(f"{WIDTH} and {HEIGHT} isn't coprime numbers!")
    exit()

data = numpy.zeros((HEIGHT*LINE_LENGTH, WIDTH*LINE_LENGTH, 3), dtype=numpy.uint8)
data[:][:] = BACKGROUND_COLOR

x, y = 0, 0
iters = 0
x_vel = LINE_LENGTH
y_vel = LINE_LENGTH

# create pattern on field
while True:
    # draw line or pixel
    if iters % 2 == 0:
        for i in range(LINE_LENGTH):
            if x_vel == y_vel:
                data[y + i][x + i] = LINE_COLOR
            else:
                data[y - i + LINE_LENGTH-1][x + i] = LINE_COLOR
    
    # move in next tile
    x += x_vel
    y += y_vel

    # check directons
    swaps = 0
    if x >= WIDTH*LINE_LENGTH or x <= -1:
        swaps += 1
        x -= x_vel
        x_vel = -x_vel

    if y >= HEIGHT*LINE_LENGTH or y <= -1:
        swaps += 1
        y -= y_vel
        y_vel = -y_vel

    # end drawing in corner
    if swaps == 2: break

    iters += 1

print(f'Generation done ({iters})')

# finding and exluding small figures on image
def make_custom_figure(figure_width, figure_height, *data):
    # here you can make own figure samples
    # data = ((x, y, y_vel), (x, y, y_vel), ...)

    figure = numpy.zeros((figure_width*LINE_LENGTH, figure_height*LINE_LENGTH, 3), dtype=numpy.uint8)
    figure[:][:] = BACKGROUND_COLOR
    
    for x, y, y_vel in data:
        for i in range(LINE_LENGTH):
            if y_vel == 1:
                figure[y*LINE_LENGTH + i][x*LINE_LENGTH + i] = LINE_COLOR
            else:
                figure[y*LINE_LENGTH - i + LINE_LENGTH-1][x*LINE_LENGTH + i] = LINE_COLOR

    # show sample
    # image = Image.fromarray(figure)
    # image.show()

    return figure

def exclude_figure(figure, figure_width, figure_height):
    for y in range(HEIGHT - (figure_height-1)):
        for x in range(WIDTH - (figure_width-1)):
            is_figure = True

            # compare sample to figure sample
            for cy in range(LINE_LENGTH * figure_height):
                for cx in range(LINE_LENGTH * figure_width):
                    if any(data[y*LINE_LENGTH + cy][x*LINE_LENGTH + cx][:] != figure[cy][cx][:]):
                        is_figure = False
                        break
            
            # remove figure
            if is_figure:
                for cy in range(LINE_LENGTH * figure_height):
                    for cx in range(LINE_LENGTH * figure_width):
                        data[y*LINE_LENGTH + cy][x*LINE_LENGTH + cx] = BACKGROUND_COLOR

if EXCLUDE_CIRCLES:
    circle = make_custom_figure(2, 2, (0, 0, -1), (1, 0, 1), (0, 1, 1), (1, 1, -1))
    exclude_figure(circle, 2, 2)
    print("Circles excluded")

if EXCLUDE_CROSSES:
    cross = make_custom_figure(4, 4, (0, 0, -1), (1, 0, 1), (2, 0, -1), (3, 0, 1), (0, 1, 1), (3, 1, -1), (0, 2, -1), (3, 2, 1), (0, 3, 1), (1, 3, -1), (2, 3, 1), (3, 3, -1))
    exclude_figure(cross, 4, 4)
    print("Crosses excluded")

# coloring image
if COLORED:
    x_vel = 1
    y_vel = 0

    x = 0
    y = 0
    iters = 0

    for y in range(HEIGHT*LINE_LENGTH):
        color_a = COLOR_A
        color_b = COLOR_B

        if y % (4*LINE_LENGTH) >= 2*LINE_LENGTH:
            color_a, color_b = color_b, color_a 

        for x in range(WIDTH*LINE_LENGTH):
            if all(data[y][x][:] == LINE_COLOR):
                color_a, color_b = color_b, color_a
            else:
                data[y][x] = color_a

    print("Coloring done")

image = Image.fromarray(data)
image = image.resize(RESIZE_TO, resample=Image.Resampling.BOX)

image.save('image.png')
image.show()
