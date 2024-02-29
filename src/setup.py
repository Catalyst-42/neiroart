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
    "glyphs": {    
        "WIDTH": ['int', 120, None, None],
        "HEIGHT": ['int', 120, None, None],
        "BACKGROUND_COLOR": ['color', BLACK, None, None],
        "RESIZE_TO": ['tuple', (480, 480), None, None],
        "GLYPHS": ['str', 'ĆćĈĉĊċČčcC', None, None],
    }
    
}
