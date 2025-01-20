import random
import time
import re


def false_or_filename(value):
    if isinstance(value, bool) and value == False:
        return False
    return str(value)


def glyphset(value):
    glyph_sets = {
        ":all": (
            "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKL"
            "MNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxy"
            "z{|}~⌂ ¡¢£¤¥¦§¨©ª«¬-®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆ"
            "ÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòó"
            "ôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠ"
            "ġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌō"
            "ŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹź"
            "ŻżŽžſƒơƷǺǻǼǽǾǿȘșȚțɑɸˆˇˉ˘˙˚˛˜˝;΄΅Ά·ΈΉΊΌΎΏΐΑΒΓΔ"
            "ΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξοπρς"
            "στυφχψωϊϋόύώϐϴЀЁЂЃЄЅІЇЈЉЊЋЌЍЎЏАБВГДЕЖЗИЙКЛМНО"
            "ПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъы"
            "ьэюяѐёђѓєѕіїјљњћќѝўџҐґ־אבגדהוזחטיךכלםמןנסעףפץ"
            "צקרשתװױײ׳״ᴛᴦᴨẀẁẂẃẄẅẟỲỳ‐‒–—―‗‘’‚‛“”„‟†‡•…‧‰′″‵"
            "‹›‼‾‿⁀⁄⁔⁴⁵⁶⁷⁸⁹⁺⁻ⁿ₁₂₃₄₅₆₇₈₉₊₋₣₤₧₪€℅ℓ№™Ω℮⅐⅑⅓⅔⅕⅖"
            "⅗⅘⅙⅚⅛⅜⅝⅞←↑→↓↔↕↨∂∅∆∈∏∑−∕∙√∞∟∩∫≈≠≡≤≥⊙⌀⌂⌐⌠⌡─│┌┐└"
            "┘├┤┬┴┼═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬▀▁▄█▌▐░▒▓■"
            "□▪▫▬▲►▼◄◊○●◘◙◦☺☻☼♀♂♠♣♥♦♪♫✓ﬁﬂ�╪╫"
        ),
        ":english": (
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "abcdefghijklmnopqrstuvwxyz"
        ),
        ":russian": (
            "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
            "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        ),
        ":greek": (
            "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρσςτυφχψω"
        ),
        ":numbers": (
            "0123456789"
        ),
        ":borders": (
            "─│┌┐└┘├┤┬┴┼═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬"
        ),
        ":punctuation": (
            "{};\\/:|<>?/~`[]()*&^%$#@!"
        ),
        ":angles": (
            "┌┐└┘"
        ),
        ":c": (
            "ĆĈĊČC"
            "ćĉċčc"
        ),
    }

    if value in glyph_sets:
        return glyph_sets[value]

    return value


def colorset(value):
    color_sets = {
        ":casual": (
            (255, 99, 132),
            (255, 159, 64),
            (255, 205, 86),
            (75, 192, 192),
            (54, 162, 235),
            (153, 102, 255),
            (201, 203, 207),
        ),
        ":grayscale": (
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
        ":red": (255, 99, 132),
        ":orange": (255, 159, 64),
        ":yellow": (255, 205, 86),
        ":green": (75, 192, 192),
        ":blue": (54, 162, 235),
        ":purple": (153, 102, 255),
        ":grey": (201, 203, 207),

        ":white": (255, 255, 255),
        ":black": (0, 0, 0),
        ":black": (21, 23, 32),
    }

    # The :color format
    if value in colors:
        return colors[value]

    # Comma separated color format
    elif re.match(r"(?:\d{1,3},){2}\d{1,3}", value):
        return tuple(
            int(c) for c in value.split(',')
        )

    # Hex color format
    elif re.match(r"#(?:[0-9A-Fa-f]{3}){1,2}", value):
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

    else:
        print(f"Color '{value}' not found")
        exit(0)


def seed(value):
    value = time.time() if value == "random" else value
    random.seed(value)

    return value
