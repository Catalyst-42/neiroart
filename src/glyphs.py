from random import choice

import numpy
from PIL import Image, ImageDraw, ImageFont

# MetaFont: https://github.com/Catalyst-42/Fonts/tree/main/MetaFont

# 12 = one symbol
MAX_X = 12*10
MAX_Y = 12*10
RESIZE_TO = (MAX_X*4, MAX_Y*4)

colors_RGB = {
    'red': (255, 99, 132),
    'orange': (255, 159, 64),
    'yellow': (255, 205, 86),
    'green': (75, 192, 192),
    'blue': (54, 162, 235),
    'purple': (153, 102, 255),
    'grey': (201, 203, 207),
    'bg': (21, 23, 32)
    }
colors_HEX = {
    'red': '#ff6384',
    'orange': '#ff9f40',
    'yellow': '#ffcd56',
    'green': '#4bc0c0',
    'blue': '#36a2eb',
    'purple': '#9966ff',
    'grey': '#c9cbcf',
    'bg': '#151720'
}
color_names = (
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'purple',
    'grey')

data = numpy.zeros((MAX_X, MAX_Y, 3), dtype=numpy.uint8)
data[:][:] = colors_RGB['bg']
image = Image.fromarray(data)

# def randcolor(): return colors_RGB[choice(color_names)]
def randhexcolor(): return colors_HEX[choice(color_names)]

glyphs = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKL" + \
         "MNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxy" + \
         "z{|}~⌂ ¡¢£¤¥¦§¨©ª«¬-®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆ" + \
         "ÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòó" + \
         "ôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠ" + \
         "ġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌō" + \
         "ŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹź" + \
         "ŻżŽžſƒơƷǺǻǼǽǾǿȘșȚțɑɸˆˇˉ˘˙˚˛˜˝;΄΅Ά·ΈΉΊΌΎΏΐΑΒΓΔ" + \
         "ΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξοπρς" + \
         "στυφχψωϊϋόύώϐϴЀЁЂЃЄЅІЇЈЉЊЋЌЍЎЏАБВГДЕЖЗИЙКЛМНО" + \
         "ПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъы" + \
         "ьэюяѐёђѓєѕіїјљњћќѝўџҐґ־אבגדהוזחטיךכלםמןנסעףפץ" + \
         "צקרשתװױײ׳״ᴛᴦᴨẀẁẂẃẄẅẟỲỳ‐‒–—―‗‘’‚‛“”„‟†‡•…‧‰′″‵" + \
         "‹›‼‾‿⁀⁄⁔⁴⁵⁶⁷⁸⁹⁺⁻ⁿ₁₂₃₄₅₆₇₈₉₊₋₣₤₧₪€℅ℓ№™Ω℮⅐⅑⅓⅔⅕⅖" + \
         "⅗⅘⅙⅚⅛⅜⅝⅞←↑→↓↔↕↨∂∅∆∈∏∑−∕∙√∞∟∩∫≈≠≡≤≥⊙⌀⌂⌐⌠⌡─│┌┐└" + \
         "┘├┤┬┴┼═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬▀▁▄█▌▐░▒▓■" + \
         "□▪▫▬▲►▼◄◊○●◘◙◦☺☻☼♀♂♠♣♥♦♪♫✓ﬁﬂ�╪╫"
# glyphs = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm{};\/:|<>?/~`[]()*&^%$#@!'
# glyphs = '─│┌┐└┘├┤┬┴┼═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬'
# glyphs = '┌┐└┘'
# glyphs = '[](){}'
# glyphs = '0123456789'
# glyphs = 'ĆćĈĉĊċČčcC'

draw = ImageDraw.Draw(image)

for x in range(MAX_X//12):
    for y in range(MAX_Y//12):
        draw.text([x*12+2, y*12+2], choice(glyphs), font=ImageFont.truetype("src/fonts/MetaFont.ttf"), fill=randhexcolor())

image = image.resize(RESIZE_TO, resample=Image.Resampling.BOX)
image.save('image.png')
image.show()
