from PIL import Image
from random import (
    randint,
    choice
)

from groups import (
    zombatar_colors,
)


def limit(value, min_value, max_value):
    random_value = randint(min_value, max_value)

    if isinstance(value, int):
        return min(max(min_value, value), max_value)
    return random_value


def solve_zcolor(value, color_space):
    colors = zombatar_colors[color_space]
    random_value = choice(tuple(colors.values()))

    if value is None:
        return random_value
    return value


def resize(image, width, height):
    image = image.resize(
        size=(width, height),
        resample=Image.Resampling.BOX
    )

    return image


def show_and_save(image, output, quiet):
    if output:
        try:
            image.save(output)
        except ValueError:
            print(f"Unknown file extension for '{output}'")
            exit(0)

    if not quiet or not output:
        image.show()
