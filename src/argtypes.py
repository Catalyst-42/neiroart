import argparse
import PIL

import random
import time
import re

import PIL.Image

from groups import (
    glyph_sets,
    colors,
    color_sets,
    zombatar_colors,
    cell_tilesets
)

# The argtypes do not resolve random values
# because this can break random number generator seed.
# So, all random values resolves in utils
# or in scripts directly.


def show_zombatar_colors(colorset):
    print(f'List of available zombatars {colorset} colors:')
    for i, color, in enumerate(zombatar_colors[colorset]):
        print(' ', i, color)

def show_bright_colors():
    show_zombatar_colors('bright')


def show_common_colors():
    show_zombatar_colors('common')


def show_skin_colors():
    show_zombatar_colors('skin')


def show_glyphsets():
    print('List of available glyphset aliases:')
    for glyphset in glyph_sets:
        print(' ', glyphset)


def show_colors():
    print('List of available colors:')
    for color, value in colors.items():
        print(' ', color, value)


def show_colorsets():
    print('List of available colorsets:')
    for colorset, values in color_sets.items():
        print(' ', colorset)


def glyphset(value):
    if value in glyph_sets:
        return glyph_sets[value]

    return value


def colorset(value):
    if isinstance(value, str):
        value = [value]

    # Resolve colorsets or single colors
    colors = []

    for c in value:
        if c in color_sets:
            colors.extend(color_sets[c])
        else:
            colors.append(color(c))

    return colors


def color(value):
    # The :color format
    if value in colors:
        return colors[value]

    # Comma separated color format
    elif re.match(r'(?:\d{1,3},){2}\d{1,3}', value):
        return tuple(
            int(c) for c in value.split(',')
        )

    # Hex color format
    elif re.match(r'#(?:[0-9A-Fa-f]{3}){1,2}', value):
        value = value[1:]  # Remove # sign

        if len(value) == 3:  # Parse #rgb type color
            value = tuple(
                int(c * 2, 16) for c in value
            )

        elif len(value) == 6:  # Parse #rrggbb type color
            value = tuple(
                int(c, 16) for c in (
                    value[:2], value[2:4], value[-2:]
            ))

        return value

    raise argparse.ArgumentTypeError(
        f"Color '{value}' not found"
    )


def seed(value):
    value = time.time() if value == ':random' else value
    value = str(value)

    random.seed(value)
    return value


def dimension(value: str):
    value = int(value)

    if not value > 0:
        raise argparse.ArgumentTypeError(
            'Image dimensions must be greater than 0'
        )

    return value


def none_or_int(value: str):
    if value.isnumeric():
        return int(value)

    elif value == ':random':
        return None

    raise argparse.ArgumentTypeError(
        "Value must be a number or ':random'"
    )


def effects(value):
    if value == "0":
        return ''
    
    elif re.match(r"[1-6]+", value):
        return value[:6]

    elif value == ':random':
        return None
    
    raise argparse.ArgumentTypeError(
        "Value must be numeric string of 1-6 numbers, 0 or ':random'"
    )


def zombatar_color(value: str, colors):
    if value == ':random':
        return None

    elif value in colors:
        return colors[value]
    
    elif value.isnumeric():
        value = min(max(0, int(value)), len(colors) - 1)
        return tuple(colors.values())[value]

    else:
        raise argparse.ArgumentTypeError(
            f"Color '{value}' not found"
        )


def zombatar_bright_color(value: str):
    return zombatar_color(value, zombatar_colors['bright'])


def zombatar_common_color(value: str):
    return zombatar_color(value, zombatar_colors['common'])


def zombatar_skin_color(value: str):
    return zombatar_color(value, zombatar_colors['skin'])


def tileset(value: str):
    if value in cell_tilesets:
        return cell_tilesets[value]

    return value
