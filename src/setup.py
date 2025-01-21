import argtypes

import argparse
import tomllib

def add_argument(argument, parser: argparse.ArgumentParser, ARGS):
    match argument:
        case 'help':
            parser.add_argument(
            '-help',
            action='help',
            default=argparse.SUPPRESS,
            help='Show all script startup parameters and exit'
        )

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

        case 'background_color':
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

def setup(script_name):
    settings = tomllib.load(open('settings.toml', 'rb'))
    ARGS = settings['global'] | settings[script_name]

    # Parse arguments
    parser = argparse.ArgumentParser(
        prog=script_name,
        add_help=False
    )
    add_argument('help', parser, ARGS)

    for argument in ARGS:
        add_argument(argument, parser, ARGS)

    parsed_args = dict(parser.parse_args()._get_kwargs())
    for arg in parsed_args:
        ARGS[arg] = parsed_args[arg]

    # Flatten nargs+ types
    if 'glyph_color_set' in ARGS:
        ARGS['glyph_color_set'] = argtypes.colorset(
            ARGS['glyph_color_set']
        )

    return ARGS
