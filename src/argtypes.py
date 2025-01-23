import argparse

import random
import time
import re


def glyphset(value):
    glyph_sets = {
        ':all': (
            '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKL'
            'MNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxy'
            'z{|}~⌂ ¡¢£¤¥¦§¨©ª«¬-®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆ'
            'ÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòó'
            'ôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠ'
            'ġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌō'
            'ŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹź'
            'ŻżŽžſƒơƷǺǻǼǽǾǿȘșȚțɑɸˆˇˉ˘˙˚˛˜˝;΄΅Ά·ΈΉΊΌΎΏΐΑΒΓΔ'
            'ΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξοπρς'
            'στυφχψωϊϋόύώϐϴЀЁЂЃЄЅІЇЈЉЊЋЌЍЎЏАБВГДЕЖЗИЙКЛМНО'
            'ПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъы'
            'ьэюяѐёђѓєѕіїјљњћќѝўџҐґ־אבגדהוזחטיךכלםמןנסעףפץ'
            'צקרשתװױײ׳״ᴛᴦᴨẀẁẂẃẄẅẟỲỳ‐‒–—―‗‘’‚‛“”„‟†‡•…‧‰′″‵'
            '‹›‼‾‿⁀⁄⁔⁴⁵⁶⁷⁸⁹⁺⁻ⁿ₁₂₃₄₅₆₇₈₉₊₋₣₤₧₪€℅ℓ№™Ω℮⅐⅑⅓⅔⅕⅖'
            '⅗⅘⅙⅚⅛⅜⅝⅞←↑→↓↔↕↨∂∅∆∈∏∑−∕∙√∞∟∩∫≈≠≡≤≥⊙⌀⌂⌐⌠⌡─│┌┐└'
            '┘├┤┬┴┼═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬▀▁▄█▌▐░▒▓■'
            '□▪▫▬▲►▼◄◊○●◘◙◦☺☻☼♀♂♠♣♥♦♪♫✓ﬁﬂ�╪╫'
        ),
        ':english': (
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            'abcdefghijklmnopqrstuvwxyz'
        ),
        ':russian': (
            'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
            'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        ),
        ':greek': (
            'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρσςτυφχψω'
        ),
        ':numbers': (
            '0123456789'
        ),
        ':borders': (
            '─│┌┐└┘├┤┬┴┼═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬'
        ),
        ':punctuation': (
            '{};\\/:|<>?/~`[]()*&^%$#@!'
        ),
        ':angles': (
            '┌┐└┘'
        ),
        ':c': (
            'ĆĈĊČC'
            'ćĉċčc'
        ),
    }

    if value in glyph_sets:
        return glyph_sets[value]

    return value


def colorset(value):
    color_sets = {
        ':casual': (
            (255, 99, 132),
            (255, 159, 64),
            (255, 205, 86),
            (75, 192, 192),
            (54, 162, 235),
            (153, 102, 255),
            (201, 203, 207),
        ),
        ':grayscale': (
            tuple((c, c, c) for c in range(0, 256, 32))
        ),
    }

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
    colors = {
        ':red': (255, 99, 132),
        ':orange': (255, 159, 64),
        ':yellow': (255, 205, 86),
        ':green': (75, 192, 192),
        ':blue': (54, 162, 235),
        ':purple': (153, 102, 255),
        ':grey': (201, 203, 207),

        ':white': (255, 255, 255),
        ':black': (0, 0, 0),
        ':black': (21, 23, 32),
    }

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
    value = time.time() if value == 'random' else value
    random.seed(value)  # Set seed

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

    elif value == 'random':
        return None

    raise argparse.ArgumentTypeError(
        "Value must be a number or 'random'"
    )


def effects(value):
    if value == "0":
        return ''
    
    elif re.match(r"[1-6]+", value):
        return value[:6]

    elif value == 'random':
        return None
    
    raise argparse.ArgumentTypeError(
        "Value must be numeric string of 1-6 numbers, 0 or 'random'"
    )

def zombatar_color(value: str, colors):
    if value in colors:
        return colors[value]
    
    elif value.isnumeric() and 0 <= int(value) - 1 < len(colors):
        return tuple(colors.values())[int(value) - 1]

    elif value == 'random':
        return random.choice(tuple(colors.values()))

    else:
        raise argparse.ArgumentTypeError(
            f"Color '{value}' not found"
        )

def zombatar_bright_color(value: str):
    colors = {
        ':white': (0, 0, 0),
        ':red': (358, 92, -8),
        ':pink': (312, 64, -4),
        ':bright-pink': (284, 21, -2),
        ':purple': (273, 77, -6),
        ':blue': (244, 69, -6),
        ':magenta': (209, 69, -6),
        ':light-cyan': (188, 20, -2),
        ':cyan': (179, 79, -8),
        ':green': (136, 92, -15),
        ':light-green': (90, 83, -26),
        ':dark-green': (136, 89, -44),
        ':yellow': (59, 83, -4),
        ':brown': (46, 91, -12),
        ':orange': (25, 90, -6),
        ':calamansi': (59, 29, -4),
        ':coffe': (37, 48, -28),
        ':dark-red': (358, 89, -39)
    }

    return zombatar_color(value, colors)


def zombatar_common_color(value: str):
    colors = {
        ':white': (0, 0, 0),
        ':dark-red': (0, 78, -42),
        ':red': (0, 73, -23),
        ':orange': (22, 78, -15),
        ':calamansi': (60, 31, -2),
        ':pale-yellow': (48, 64, -7),
        ':bright-coffe': (36, 60, -36),
        ':coffe': (32, 70, -59),
        ':brown': (26, 94, -73),
        ':dark': (207, 18, -77),
        ':black': (240, 100, -97),
        ':water': (180, 17, -7),
        ':blue': (224, 74, -6),
        ':mint': (163, 94, -22),
        ':foliage-green': (69, 90, -29),
        ':light-green': (131, 86, -19),
        ':pink': (298, 72, -11),
        ':purple': (270, 77, -21)
    }

    return zombatar_color(value, colors)


def zombatar_skin_color(value: str):
    colors = {
        ':skin-1': (91, 17, -43),
        ':skin-2': (136, 41, -48),
        ':skin-3': (71, 30, -48),
        ':skin-4': (67, 62, 50),
        ':skin-5': (67, 35, -37),
        ':skin-6': (83, 93, -42),
        ':skin-7': (101, 62, -45),
        ':skin-8': (83, 93, -42),
        ':skin-9': (100, 41, -35),
        ':skin-10': (125, 58, -40),
        ':skin-11': (125, 40, -31),
        ':skin-12': (92, 25, -53)
    }

    return zombatar_color(value, colors)
