import PIL
import numpy as np
import random


def limit_or_random(value, min_value, max_value):
    if isinstance(value, int):
        random.randint(min_value, max_value)  # Normalize random
        return min(max(min_value, value), max_value)
    return random.randint(min_value, max_value)


def resize(image, width, height):
    image = image.resize(
        size=(width, height),
        resample=PIL.Image.Resampling.BOX
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
