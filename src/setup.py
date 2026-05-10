import argparse
import tomllib

import argtypes
import aliases

# This setup file configures all parameters for argparse
# for all scripts. Default values stored in settings.toml,
# allaliases for values stored in groups.py 


def add_argument(argument, parser, ARGS, script_name):
    match argument:
        # Helper arguments
        case 'help':
            parser.add_argument(
            '-help', '--help',
            action='help',
            default=argparse.SUPPRESS,
            help='Show all script startup parameters and exit'
        )

        case 'show_glyphsets':
            parser.add_argument(
                '--show-glyphsets',
                help=(
                    'Show list of all available glyphs '
                    'aliases with values'
                ),
                action='store_true',
            )

        case 'show_colors':
            parser.add_argument(
                '--show-colors',
                help=(
                    'Show list of all available color '
                    'aliases with values'
                ),
                action='store_true',
            )

        case 'show_colorsets':
            parser.add_argument(
                '--show-colorsets',
                help=(
                    'Show list of all available colorsets '
                    'aliases with values'
                ),
                action='store_true',
            )

        case 'show_bright_colors':
            parser.add_argument(
                '--show-bright-colors',
                help=(
                    'Show list of all available bright '
                    'color aliases with values'
                ),
                action='store_true',
            )

        case 'show_common_colors':
            parser.add_argument(
                '--show-common-colors',
                help=(
                    'Show list of all available common '
                    'color aliases with values'
                ),
                action='store_true',
            )

        case 'show_skin_colors':
            parser.add_argument(
                '--show-skin-colors',
                help=(
                    'Show list of all available skin '
                    'color aliases with values'
                ),
                action='store_true',
            )

        case 'show_tilesets':
            parser.add_argument(
                '--show-tilesets',
                help=(
                    'Show list of all available tilesets '
                    'for mapper script'
                ),
                action='store_true',
            )

        # Global arguments
        case 'seed':
            parser.add_argument(
                '-s', '--seed',
                help=(
                    'Seed for random number generator. '
                    'Can be :random or any other string '
                    'to lock the seed'
                ),
                default=ARGS['seed'],
                type=argtypes.seed,
                dest='seed',
            )

        case 'show_seed':
            parser.add_argument(
                '-ss', '--show-seed',
                help='Display script current seed value',
                action='store_const',
                const=not ARGS['show_seed'],
                default=ARGS['show_seed'],
                dest='show_seed',
            )

        case 'quiet':
            parser.add_argument(
                '-q',
                help=(
                    'Do not show result image. Disabled if '
                    'no output image specified'
                ),
                action='store_const',
                const=not ARGS['quiet'],
                default=ARGS['quiet'],
                dest='quiet',
            )

        case 'output':
            parser.add_argument(
                '-o',
                help=(
                    'Output image, must be with image extension '
                    'such as .png, .jpeg, .bmp or other'
                ),
                default=ARGS['output'],
                type=str,
                dest='output',
            )

        # Glyphs
        case 'font_name':
            parser.add_argument(
                '-f', '-fn',
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

        case 'font_padding':
            parser.add_argument(
                '-p', '-fp', '-fm',
                help='Gap between glyphs on image',
                default=ARGS['font_padding'],
                type=int,
                dest='font_padding',
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

        case 'random_order':
            parser.add_argument(
                '-r',
                help='Render glyphs in a random order or not',
                action='store_false',
                dest='random_order'
            )

        case 'glyphset':
            parser.add_argument(
                '-g',
                help='List of symbols that will make up the image',
                default=ARGS['glyphset'],
                type=argtypes.glyphset,
                dest='glyphset',
            )

        case 'glyph_colorset':
            parser.add_argument(
                '-gc',
                help=(
                    'List of colors for glyphs. '
                    'Can accept #rrggbb, #rgb, r,g,b or :alias values'
                ),
                default=ARGS['glyph_colorset'],
                type=str,
                dest='glyph_colorset',
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

        case 'image_width' if script_name != 'coprimes':
            parser.add_argument(
                '-w',
                help=(
                    'Image width. Can be parametrized with -as '
                    'flag as pixels or tiles (if available)'
                ),
                default=ARGS['image_width'],
                type=argtypes.dimension,
                dest='image_width',
            )

        case 'image_height' if script_name != 'coprimes':
            parser.add_argument(
                '-h',
                help=(
                    'Image height. Can be parametrized with -as '
                    'flag as pixels or tiles (if available)'
                ),
                default=ARGS['image_height'],
                type=argtypes.dimension,
                dest='image_height',
            )

        case 'by':
            parser.add_argument(
                '-by',
                help='The size unit for image width and height',
                default=ARGS['by'],
                choices=('pixels', 'tiles'),
                dest='by',
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
                metavar='EFFECTS: 1-6 | 0',
                help='String of enemy effects by indexes',
                default=ARGS['effects'],
                type=argtypes.effects,
                dest='effects',
            )

        # Zombatars
        case 'background':
            parser.add_argument(
                '-bg',
                metavar='BACKGROUND: 1-5',
                help='Type of image background',
                default=ARGS['background'],
                type=argtypes.none_or_int,
                dest='background',
            )

        case 'background_color':
            parser.add_argument(
                '-bgc',
                metavar='BACKGROUND_COLOR: 1-18 | BRIGHT_COLOR',
                help=(
                    'Background color index '
                    'for background of 1 type'
                ),
                default=ARGS['background_color'],
                type=argtypes.zombatar_bright_color,
                dest='background_color',
            )

        case 'skin_color':
            parser.add_argument(
                '-sc',
                metavar='SKIN_COLOR: 1-12 | SKIN_COLOR',
                help='Zombie skin color index',
                default=ARGS['skin_color'],
                type=argtypes.zombatar_skin_color,
                dest='skin_color',
            )

        case 'cloth':
            parser.add_argument(
                '-c',
                metavar='CLOTH: 0-12',
                help='Zombie cloth element',
                default=ARGS['cloth'],
                type=argtypes.none_or_int,
                dest='cloth',
            )

        case 'tidbit':
            parser.add_argument(
                '-t',
                metavar='TIDBIT: 0-14',
                help='Zombie tidbit element',
                default=ARGS['tidbit'],
                type=argtypes.none_or_int,
                dest='tidbit',
            )

        case 'tidbit_color':
            parser.add_argument(
                '-tc',
                metavar='TIDBIT_COLOR: 1-18 | BRIGHT_COLOR',
                help=(
                    'Color index of tidbit for '
                    '2, 3, 10, 11 and 12 type of them'
                ),
                default=ARGS['tidbit_color'],
                type=argtypes.zombatar_bright_color,
                dest='tidbit_color',
            )

        case 'accessory':
            parser.add_argument(
                '-a',
                metavar='ACCESSORY: 0-16',
                help='Zombie accessory element',
                default=ARGS['accessory'],
                type=argtypes.none_or_int,
                dest='accessory',
            )

        case 'accessory_color':
            parser.add_argument(
                '-ac',
                metavar='ACCESSORY_COLOR: 1-18 | BRIGHT_COLOR',
                help=(
                    'Color index of accessory for '
                    '9, 11, 13 and 14 types of them'
                ),
                default=ARGS['accessory_color'],
                type=argtypes.zombatar_bright_color,
                dest='accessory_color',
            )

        case 'mustache':
            parser.add_argument(
                '-m',
                metavar='MUSTACHE: 0-24',
                help='Zombie mustache element',
                default=ARGS['mustache'],
                type=argtypes.none_or_int,
                dest='mustache',
            )

        case 'mustache_color':
            parser.add_argument(
                '-mc',
                metavar='MUSTACHE_COLOR: 1-18 | COMMON_COLOR',
                help='Zombie mustache color index',
                default=ARGS['mustache_color'],
                type=argtypes.zombatar_common_color,
                dest='mustache_color',
            )

        case 'hair':
            parser.add_argument(
                '-h',
                metavar='HAIR: 0-16',
                help='Zombie hair element',
                default=ARGS['hair'],
                type=argtypes.none_or_int,
                dest='hair',
            )

        case 'hair_color':
            parser.add_argument(
                '-hc',
                metavar='HAIR_COLOR: 1-18 | COMMON_COLOR',
                help='Zombie hair color index',
                default=ARGS['hair_color'],
                type=argtypes.zombatar_common_color,
                dest='hair_color',
            )

        case 'eyewear':
            parser.add_argument(
                '-e',
                metavar='EYEWEAR: 0-16',
                help='Zombie eyewear element',
                default=ARGS['eyewear'],
                type=argtypes.none_or_int,
                dest='eyewear',
            )

        case 'eyewear_color':
            parser.add_argument(
                '-ec',
                metavar='EYEWEAR_COLOR: 1-18 | BRIGHT_COLOR',
                help=(
                    'Color index of eyewear which eyewear '
                    'type is less than 13'
                ),
                default=ARGS['eyewear_color'],
                type=argtypes.zombatar_bright_color,
                dest='eyewear_color',
            )

        case 'hat':
            parser.add_argument(
                '-hat',
                metavar='HAT: 0-14',
                help='Zombie hat element',
                default=ARGS['hat'],
                type=argtypes.none_or_int,
                dest='hat',
            )

        case 'hat_color':
            parser.add_argument(
                '-hatc',
                metavar='HAT_COLOR: 1-18 | BRIGHT_COLOR',
                help='Color index of hat if it\'s not 13 type',
                default=ARGS['hat_color'],
                type=argtypes.zombatar_bright_color,
                dest='hat_color',
            )

        # Mapper
        case 'show_tiles':
            parser.add_argument(
                '-d', '--show_tiles',
                help='Draw tileset in top left corner',
                action='store_const',
                const=not ARGS['show_tiles'],
                default=ARGS['show_tiles'],
                dest='show_tiles'
            )

        case 'tileset':
            parser.add_argument(
                '-t',
                help=(
                    'Tile view style. Can be '
                    'tile :alias or path to fileset file'
                ),
                default=ARGS['tileset'],
                type=argtypes.tileset,
                dest='tileset',
            )

        case 'tile_limit':
            parser.add_argument(
                '-l', '-tl', '-lim',
                help='Limit number of tiles to be generated',
                default=ARGS['tile_limit'],
                type=int,
                dest='tile_limit',
            )

        case 'tile_padding':
            parser.add_argument(
                '-p', '-tp',
                help='Padding between tiles on canvas',
                default=ARGS['tile_padding'],
                type=int,
                dest='tile_padding',
            )

        case 'colorset':
            parser.add_argument(
                '-c',
                help=(
                    'List of colors for tiles. '
                    'Can accept #rrggbb, #rgb, r,g,b or :alias values'
                ),
                default=ARGS['colorset'],
                type=str,
                dest='colorset',
                nargs='+'
            )

        case 'color_style':
            parser.add_argument(
                '-m', '-cs',
                help=(
                    'Cell coloring style. May be '
                    ":random, :pulse or :spot"
                ),
                default=ARGS["color_style"],
                type=str,
                choices=(':random', ':pulse', ':spot'),
                dest="color_style",
            )

        # Worm
        case 'move_straight':
            parser.add_argument(
                '-ms',
                help='Allow worm to move straight',
                action='store_const',
                const=not ARGS['move_straight'],
                default=ARGS['move_straight'],
                dest='move_straight'
            )

        case 'move_diagonal':
            parser.add_argument(
                '-md',
                help='Allow worm to move diagonally',
                action='store_const',
                const=not ARGS['move_diagonal'],
                default=ARGS['move_diagonal'],
                dest='move_diagonal'
            )

        case 'move_backwards':
            parser.add_argument(
                '-mb',
                help='Allow worm to move backwards to prevous position',
                action='store_const',
                const=not ARGS['move_backwards'],
                default=ARGS['move_backwards'],
                dest='move_backwards'
            )

        case 'step_min_length':
            parser.add_argument(
                '-smin',
                help='Worm step minimum length',
                default=ARGS['step_min_length'],
                type=int,
                dest='step_min_length',
            )

        case 'step_max_length':
            parser.add_argument(
                '-smax',
                help='Worm step maximum length',
                default=ARGS['step_max_length'],
                type=int,
                dest='step_max_length',
            )

        case 'step_limit':
            parser.add_argument(
                '-l', '-sl', '-lim',
                help='Number of steps for worm to move',
                default=ARGS['step_limit'],
                type=int,
                dest='step_limit',
            )

        case 'colorset':
            parser.add_argument(
                '-c', '-sc',
                help=(
                    'List of colors for step pixels. '
                    'Can accept #rrggbb, #rgb, r,g,b or :alias values'
                ),
                default=ARGS['colorset'],
                type=str,
                dest='colorset',
                nargs='+'
            )

        # Coprimes
        case 'line_length':
            parser.add_argument(
                '-l', '-ll',
                help='Length of one step',
                default=ARGS['line_length'],
                type=int,
                dest='line_length',
            )

        case 'line_thickness':
            parser.add_argument(
                '-t', '-lt',
                help='Thickness of line',
                default=ARGS['line_thickness'],
                type=int,
                dest='line_thickness',
            )

        case 'line_color' if script_name == 'coprimes':
            parser.add_argument(
                '-c', '-lc',
                help='Color of dashes',
                default=ARGS['line_color'],
                type=argtypes.color,
                dest='line_color',
            )

        case 'background_color_a':
            parser.add_argument(
                '-bga',
                help='First background color',
                default=ARGS['background_color_a'],
                type=argtypes.color,
                dest='background_color_a',
            )

        case 'background_color_b':
            parser.add_argument(
                '-bgb',
                help='Second background color',
                default=ARGS['background_color_b'],
                type=argtypes.color,
                dest='background_color_b',
            )

        case 'exclude':
            parser.add_argument(
                '-e',
                help='Exclude figure segments on image',
                default=ARGS['exclude'],
                dest='exclude',
                choices=list(aliases.figures.keys()),
                nargs='+'
            )

        case 'image_width':
            parser.add_argument(
                '-w',
                help=(
                    'Base image width in tiles based on line '
                    'length. Must be coprime with image height'
                ),
                default=ARGS['image_width'],
                type=argtypes.coprime,
                dest='image_width',
            )

        case 'image_height':
            parser.add_argument(
                '-h',
                help=(
                    'Base image height in tiles based on line '
                    'length. Must be coprime with image height'
                ),
                default=ARGS['image_height'],
                type=argtypes.coprime,
                dest='image_height',
            )

        # Puzzles
        case 'tile_side':
            parser.add_argument(
                '-t', '-p',
                help='Side of one puzzle in pixels',
                default=ARGS['tile_side'],
                type=int,
                dest='tile_side',
            )

        case 'ledge_length':
            parser.add_argument(
                '-l',
                help='Length of puzzle ledge in pixels',
                default=ARGS['ledge_length'],
                type=int,
                dest='ledge_length',
            )

        case 'ledge_depth':
            parser.add_argument(
                '-d',
                help='Depth of puzzle ledge in pixels',
                default=ARGS['ledge_depth'],
                type=int,
                dest='ledge_depth',
            )

        case 'line_color':
            parser.add_argument(
                '-lc',
                help='Color of puzzle border',
                default=ARGS['line_color'],
                type=argtypes.color,
                dest='line_color',
            )


def setup(script_name):
    settings = tomllib.load(open('settings.toml', 'rb'))
    ARGS = settings['global'] | settings[script_name]

    helps = {
        'zombatars': {
            'show_bright_colors': argtypes.show_bright_colors,
            'show_common_colors': argtypes.show_common_colors,
            'show_skin_colors': argtypes.show_skin_colors
        },
        'glyphs': {
            'show_glyphsets': argtypes.show_glyphsets,
            'show_colors': argtypes.show_colors,
            'show_colorsets': argtypes.show_colorsets
        },
        'mapper': {
            'show_colors': argtypes.show_colors,
            'show_colorsets': argtypes.show_colorsets,
            'show_tilesets': argtypes.show_tilesets
        },
        'worm': {
            'show_colors': argtypes.show_colors,
            'show_colorsets': argtypes.show_colorsets
        },
        'coprimes': {
            'show_colors': argtypes.show_colors
        },
        'puzzles': {
            'show_colors': argtypes.show_colors,
            'show_colorsets': argtypes.show_colorsets
        }
    }.get(script_name, dict())

    # Parse arguments
    parser = argparse.ArgumentParser(
        prog=script_name,
        add_help=False
    )

    for argument in ('help', *helps, *tuple(ARGS)):
        add_argument(argument, parser, ARGS, script_name)

    ARGS.update(dict(parser.parse_args()._get_kwargs()))

    # Resolve nargs+ type values
    if 'colorset' in ARGS:
        ARGS['colorset'] = argtypes.colorset(ARGS['colorset'])

    # Display seed
    if ARGS['show_seed'] and script_name != "coprimes":
        print(f'Seed: {ARGS['seed']}')

    # Dislpay help for aliases and exit
    [helps[helper]() for helper in helps if ARGS[helper]]
    if any([ARGS[helper] for helper in helps]):
        exit(0)

    # print(ARGS)
    return ARGS
