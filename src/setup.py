import argparse
import tomllib

import argtypes

def add_argument(argument, parser: argparse.ArgumentParser, ARGS, script_name):
    match argument:
        # Helper arguments
        case 'help':
            parser.add_argument(
            '-help',
            action='help',
            default=argparse.SUPPRESS,
            help='Show all script startup parameters and exit'
        )

        # Global arguments
        case 'seed':
            parser.add_argument(
                '-s', '-seed',
                help="Seed for random number generator. Can be 'random' or any other string to lock the seed",
                default=ARGS['seed'],
                type=argtypes.seed,
                dest='seed',
            )

        case 'quiet':
            parser.add_argument(
                '-q',
                help='Do not show result image. Disabled if no output image specified',
                action='store_const',
                const=not ARGS['quiet'],
                default=ARGS['quiet'],
                dest='quiet',
            )

        case 'output':
            parser.add_argument(
                '-o',
                help='Output image, must be with image extension such as .png, .jpeg, .bmp or other',
                default=ARGS['output'],
                type=str,
                dest='output',
            )

        # Glyphs
        case 'font_name':
            parser.add_argument(
                '-fn',
                help='Set up font by given name',
                default=ARGS['font_name'],
                type=str,
                dest='font_name',
            )

        case 'font_size':
            parser.add_argument(
                '-fs',
                help='Set up font size',
                default=ARGS['font_size'],
                type=int,
                dest='font_size',
            )

        case 'font_margin':
            parser.add_argument(
                '-fm',
                help='Gap between glyphs on image',
                default=ARGS['font_margin'],
                type=int,
                dest='font_margin',
            )

        case 'font_aliasing':
            parser.add_argument(
                '-fa',
                help='Alias font on render',
                action='store_const',
                const=not ARGS['font_aliasing'],
                default=ARGS['font_aliasing'],
                dest='font_aliasing',
            )

        case 'glyph_set':
            parser.add_argument(
                '-g',
                help='List of symbols that will make up the image',
                default=ARGS['glyph_set'],
                type=argtypes.glyphset,
                dest='glyph_set',
            )

        case 'glyph_color_set':
            parser.add_argument(
                '-gc',
                help='List of colors for glyphs',
                default=ARGS['glyph_color_set'],
                type=str,
                dest='glyph_color_set',
                nargs='+'
            )

        case 'background_color' if script_name != 'zombatars':
            parser.add_argument(
                '-bg',
                help='Image background color',
                default=ARGS['background_color'],
                type=argtypes.color,
                dest='background_color',
            )

        case 'image_width':
            parser.add_argument(
                '-w',
                help='List of symbols that will make up the image',
                default=ARGS['image_width'],
                type=argtypes.dimension,
                dest='image_width',
            )

        case 'image_height':
            parser.add_argument(
                '-h',
                help='List of symbols that will make up the image',
                default=ARGS['image_height'],
                type=argtypes.dimension,
                dest='image_height',
            )

        case 'image_scale_factor':
            parser.add_argument(
                '-x',
                help='Final image scale multiplier',
                default=ARGS['image_scale_factor'],
                type=int,
                dest='image_scale_factor',
            )

        # Enemies
        case 'face':
            parser.add_argument(
                '-f',
                metavar='FACE: 1-31',
                help='Enemy face icon',
                default=ARGS['face'],
                type=argtypes.none_or_int,
                dest='face',
            )

        case 'level':
            parser.add_argument(
                '-l',
                metavar='LEVEL: 0-99',
                help='Enemy level',
                default=ARGS['level'],
                type=argtypes.none_or_int,
                dest='level',
            )

        case 'hp':
            parser.add_argument(
                '-hp',
                metavar='HP: 1-999',
                help='Enemy current hp',
                default=ARGS['hp'],
                type=argtypes.none_or_int,
                dest='hp',
            )

        case 'max_hp':
            parser.add_argument(
                '-mhp',
                metavar='MAX_HP: 1-909',
                help='Enemy max hp',
                default=ARGS['max_hp'],
                type=argtypes.none_or_int,
                dest='max_hp',
            )

        case 'mana':
            parser.add_argument(
                '-m',
                metavar='MANA: 0-999',
                help='Enemy current mana',
                default=ARGS['mana'],
                type=argtypes.none_or_int,
                dest='mana',
            )

        case 'max_mana':
            parser.add_argument(
                '-mm',
                metavar='MAX_MANA: 1-999',
                help='Enemy max mana',
                default=ARGS['max_mana'],
                type=argtypes.none_or_int,
                dest='max_mana',
            )

        case 'effects':
            parser.add_argument(
                '-e',
                metavar="EFFECTS: 0-5",
                help='List of enemy effects by indexes',
                default=ARGS['effects'],
                type=argtypes.effects,
                dest='effects',
            )

        # Zombatars
        case 'background':
            parser.add_argument(
                '-bg',
                metavar='BACKGROUND: 1-5',
                help='',
                default=ARGS['background'],
                type=argtypes.none_or_int,
                dest='background',
            )

        case 'background_color':
            parser.add_argument(
                '-bgc',
                metavar='BACKGROUND_COLOR: 1-18',
                help='',
                default=ARGS['background_color'],
                type=argtypes.none_or_int,
                dest='background_color',
            )

        case 'skin_color':
            parser.add_argument(
                '-sc',
                metavar='SKIN_COLOR: 1-12',
                help='',
                default=ARGS['skin_color'],
                type=argtypes.none_or_int,
                dest='skin_color',
            )

        case 'cloth':
            parser.add_argument(
                '-c',
                metavar='CLOTH: 0-12',
                help='',
                default=ARGS['cloth'],
                type=argtypes.none_or_int,
                dest='cloth',
            )

        case 'tidbit':
            parser.add_argument(
                '-t',
                metavar='TIDBIT: 0-14',
                help='',
                default=ARGS['tidbit'],
                type=argtypes.none_or_int,
                dest='tidbit',
            )

        case 'tidbit_color':
            parser.add_argument(
                '-tc',
                metavar='TIDBIT_COLOR: 1-18',
                help='',
                default=ARGS['tidbit_color'],
                type=argtypes.none_or_int,
                dest='tidbit_color',
            )

        case 'accessory':
            parser.add_argument(
                '-a',
                metavar='ACCESSORY: 0-16',
                help='',
                default=ARGS['accessory'],
                type=argtypes.none_or_int,
                dest='accessory',
            )

        case 'accessory_color':
            parser.add_argument(
                '-ac',
                metavar='ACCESSORY_COLOR: 1-18',
                help='',
                default=ARGS['accessory_color'],
                type=argtypes.none_or_int,
                dest='accessory_color',
            )

        case 'mustache':
            parser.add_argument(
                '-m',
                metavar='MUSTACHE: 0-24',
                help='',
                default=ARGS['mustache'],
                type=argtypes.none_or_int,
                dest='mustache',
            )

        case 'mustache_color':
            parser.add_argument(
                '-mc',
                metavar='MUSTACHE_COLOR: 1-18',
                help='',
                default=ARGS['mustache_color'],
                type=argtypes.none_or_int,
                dest='mustache_color',
            )

        case 'hair':
            parser.add_argument(
                '-h',
                metavar='HAIR: 0-16',
                help='',
                default=ARGS['hair'],
                type=argtypes.none_or_int,
                dest='hair',
            )

        case 'hair_color':
            parser.add_argument(
                '-hc',
                metavar='HAIR_COLOR: 1-18',
                help='',
                default=ARGS['hair_color'],
                type=argtypes.none_or_int,
                dest='hair_color',
            )

        case 'eyewear':
            parser.add_argument(
                '-e',
                metavar='EYEWEAR: 0-16',
                help='',
                default=ARGS['eyewear'],
                type=argtypes.none_or_int,
                dest='eyewear',
            )

        case 'eyewear_color':
            parser.add_argument(
                '-ec',
                metavar='EYEWEAR_COLOR: 1-18',
                help='',
                default=ARGS['eyewear_color'],
                type=argtypes.none_or_int,
                dest='eyewear_color',
            )

        case 'hat':
            parser.add_argument(
                '-hat',
                metavar='HAT: 0-14',
                help='',
                default=ARGS['hat'],
                type=argtypes.none_or_int,
                dest='hat',
            )

        case 'hat_color':
            parser.add_argument(
                '-hatc',
                metavar='HAT_COLOR: 1-18',
                help='',
                default=ARGS['hat_color'],
                type=argtypes.none_or_int,
                dest='hat_color',
            )


def setup(script_name):
    settings = tomllib.load(open('settings.toml', 'rb'))
    ARGS = settings['global'] | settings[script_name]

    # Parse arguments
    parser = argparse.ArgumentParser(
        prog=script_name,
        add_help=False
    )

    for argument in ('help', *tuple(ARGS.keys())):
        add_argument(argument, parser, ARGS, script_name)

    parsed_args = dict(parser.parse_args()._get_kwargs())
    for arg in parsed_args:
        ARGS[arg] = parsed_args[arg]

    # Flatten nargs+ types
    if 'glyph_color_set' in ARGS:
        ARGS['glyph_color_set'] = argtypes.colorset(
            ARGS['glyph_color_set']
        )

    # print(ARGS)
    return ARGS
