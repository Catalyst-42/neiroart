from colors import RGB
from colors import WHITE, BLACK

inputs = {
    "map_linear": {
        "WIDTH": ['int', 256, None, None],
        "HEIGHT": ['int', 256, None, None],
        "COLOR": ['color', RGB['purple'], None, None],
        "SWITCH_COLORS": ['colors', (RGB['yellow'], RGB['red'], RGB['green']), None, None],
        "BACKGROUND_COLOR": ['color', BLACK, None, None],
        "MAX_ITERS": ['int', 512, None, None],
        "RESIZE_TO": ['tuple', (512, 512), None, None],
    },
    "map_simple": {
        "WIDTH": ['int', 256, None, None],
        "HEIGHT": ['int', 256, None, None],
        "COLORS": ['colors', (WHITE, ), None, None],
        "BACKGROUND_COLOR": ['color', BLACK, None, None],
        "STEP_LENGTH_MIN": ['int', 1, None, None],
        "STEP_LENGTH_MAX": ['int', 1, None, None],
        "MAX_ITERS": ['int', 8192, None, None],
        "RESIZE_TO": ['tuple', (256*2, 256*2), None, None],
    },
    "map_squared": {
        "WIDTH": ['int', 256, None, None],
        "HEIGHT": ['int', 256, None, None],
        "COLOR": ['color', RGB['purple'], None, None],
        "SWITCH_COLORS": ['colors', [RGB[color] for color in RGB.keys()], None, None],
        "BACKGROUND_COLOR": ['color', BLACK, None, None],
        "MAX_ITERS": ['int', 512, None, None],
        "RESIZE_TO": ['tuple', (256*2, 256*2), None, None],
    },
    "glyphs": {
        "WIDTH": ['int', 120, None, None],
        "HEIGHT": ['int', 120, None, None],
        "BACKGROUND_COLOR": ['color', BLACK, None, None],
        "RESIZE_TO": ['tuple', (480, 480), None, None],
        "GLYPHS": ['str', 'ĆćĈĉĊċČčcC', None, None],
    },
    "zombatar": {
        "RESIZE_TO": ['tuple', (512, 512), None, None],
    },
    "enemies": {
        "RESIZE_TO": ['tuple', (512, 256), None, None],
    },
    "puzzles": {
        "WIDTH": ['int', 16*8 + 1, None, None],
        "HEIGHT": ['int', 16*8 + 1, None, None],
        "LINE_COLOR": ['color', BLACK, None, None],
        "BACKGROUND_COLOR": ['color', WHITE, None, None],
        "COLORED": ['bool', True, None, None],
        "CELL_COLORS": ['colors', [RGB['purple'], RGB['yellow']], None, None],
        "RESIZE_TO": ['tuple', (1032, 1032), None, None],
    },
    "primes": {
        "WIDTH": ['int', 23, None, None],
        "HEIGHT": ['int', 13, None, None],
        "LINE_LENGTH": ['int', 3, None, None],
        "LINE_COLOR": ['color', BLACK, None, None],
        "BACKGROUND_COLOR": ['color', WHITE, None, None],
        "COLORED": ['bool', True, None, None],
        "COLOR_A": ['color', RGB['purple'], None, None],
        "COLOR_B": ['color', RGB['yellow'], None, None],
        "EXCLUDE_CIRCLES": ['bool', False, None, None],
        "EXCLUDE_CROSSES": ['bool', False, None, None],
        "RESIZE_TO": ['tuple', (138, 78), None, None],
    }
}
