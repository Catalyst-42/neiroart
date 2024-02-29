from colors import RGB, BLACK
from PIL import Image, ImageDraw, ImageFont
from random import choice

from setup import inputs
import numpy

# MetaFont: https://github.com/Catalyst-42/Fonts/tree/main/MetaFont

def gen():
    CONSTANTS = inputs['glyphs']
    
    # 12 = one symbol
    WIDTH = CONSTANTS['WIDTH'][1]
    HEIGHT = CONSTANTS['HEIGHT'][1]

    BACKGROUND_COLOR = CONSTANTS['BACKGROUND_COLOR'][1]

    RESIZE_TO = CONSTANTS['RESIZE_TO'][1]
    GLYPHS = CONSTANTS['GLYPHS'][1]

    # GLYPHS = (
    #     "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKL"
    #     "MNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxy"
    #     "z{|}~⌂ ¡¢£¤¥¦§¨©ª«¬-®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆ"
    #     "ÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòó"
    #     "ôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠ"
    #     "ġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌō"
    #     "ŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹź"
    #     "ŻżŽžſƒơƷǺǻǼǽǾǿȘșȚțɑɸˆˇˉ˘˙˚˛˜˝;΄΅Ά·ΈΉΊΌΎΏΐΑΒΓΔ"
    #     "ΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξοπρς"
    #     "στυφχψωϊϋόύώϐϴЀЁЂЃЄЅІЇЈЉЊЋЌЍЎЏАБВГДЕЖЗИЙКЛМНО"
    #     "ПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъы"
    #     "ьэюяѐёђѓєѕіїјљњћќѝўџҐґ־אבגדהוזחטיךכלםמןנסעףפץ"
    #     "צקרשתװױײ׳״ᴛᴦᴨẀẁẂẃẄẅẟỲỳ‐‒–—―‗‘’‚‛“”„‟†‡•…‧‰′″‵"
    #     "‹›‼‾‿⁀⁄⁔⁴⁵⁶⁷⁸⁹⁺⁻ⁿ₁₂₃₄₅₆₇₈₉₊₋₣₤₧₪€℅ℓ№™Ω℮⅐⅑⅓⅔⅕⅖"
    #     "⅗⅘⅙⅚⅛⅜⅝⅞←↑→↓↔↕↨∂∅∆∈∏∑−∕∙√∞∟∩∫≈≠≡≤≥⊙⌀⌂⌐⌠⌡─│┌┐└"
    #     "┘├┤┬┴┼═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬▀▁▄█▌▐░▒▓■"
    #     "□▪▫▬▲►▼◄◊○●◘◙◦☺☻☼♀♂♠♣♥♦♪♫✓ﬁﬂ�╪╫"
    # )
    # GLYPHS = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm{};\/:|<>?/~`[]()*&^%$#@!'
    # GLYPHS = '─│┌┐└┘├┤┬┴┼═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬'
    # GLYPHS = '┌┐└┘'
    # GLYPHS = '[](){}'
    # GLYPHS = '0123456789'
    # GLYPHS = 'ĆćĈĉĊċČčcC'
    
    data = numpy.zeros((HEIGHT, WIDTH, 3), dtype=numpy.uint8)
    data[:][:] = BACKGROUND_COLOR
    image = Image.fromarray(data)

    def random_color(): 
        return RGB[choice(tuple(RGB.keys()))]

    draw = ImageDraw.Draw(image)
    for x in range(WIDTH // 12):
        for y in range(HEIGHT // 12):
            draw.text((x*12 + 2, y*12 + 2), choice(GLYPHS), font=ImageFont.truetype("fonts/MetaFont.ttf"), fill=random_color())

    image = image.resize(RESIZE_TO, resample=Image.Resampling.BOX)
    image.save('image.png')
    image.show()
