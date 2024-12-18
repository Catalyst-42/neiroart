from colors import RGB, BLACK
from PIL import Image, ImageDraw, ImageFont
from random import choice

import numpy

# MetaFont: https://github.com/Catalyst-42/Fonts/tree/main/MetaFont

FONTSIZE = 12

# 12 = one symbol
WIDTH = 10
HEIGHT = 10

GLYPHS = "borders"
BACKGROUND_COLOR = BLACK

RESIZE_TO = (WIDTH * 4 * FONTSIZE, HEIGHT * 4 * FONTSIZE)

sets = {
    "all": (
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
    "english": (
        "QWERTYUIOPASDFGHJKLZXCVBNM"
        "qwertyuiopasdfghjklzxcvbnm"
        "{};\\/:|<>?/~`[]()*&^%$#@!"
    ),
    "borders": (
        "┌┐└┘"
    ),
    "borders-all": (
        "─│┌┐└┘├┤┬┴┼═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬"
    ),
    "brackets": (
        "[](){}"
    ),
    "numbers": (
        "0123456789"
    ),
    "c": (
        "ĆćĈĉĊċČčcC"
    ),
}

if GLYPHS in sets:
    GLYPHS = sets[GLYPHS]

data = numpy.zeros((HEIGHT * FONTSIZE, WIDTH * FONTSIZE, 3), dtype=numpy.uint8)
data[:][:] = BACKGROUND_COLOR
image = Image.fromarray(data)

def random_color(): 
    return RGB[choice(tuple(RGB.keys()))]

draw = ImageDraw.Draw(image)
for x in range(WIDTH):
    for y in range(HEIGHT):
        draw.text(
            (x*FONTSIZE + 2, y*FONTSIZE + 2),
            choice(GLYPHS),
            font=ImageFont.truetype("fonts/MetaFont.ttf"),
            fill=random_color()
        )

image = image.resize(RESIZE_TO, resample=Image.Resampling.BOX)
image.save('image.png')
image.show()
