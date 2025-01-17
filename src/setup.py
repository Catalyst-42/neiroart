import argparse
import tomllib

def add_argument(argument, parser, ARGS):
    match argument:
        case "help":
            parser.add_argument(
            "-help",
            action="help",
            default=argparse.SUPPRESS,
            help="Show all script startup parameters and exit"
        )

        case "font_size":
            parser.add_argument(
                "-fs",
                help="Set up font size",
                default=ARGS["font_size"],
                type=int,
                dest="font_size",
            )

        case "font_margin":
            parser.add_argument(
                "-fm",
                help="Gap between glyphs on image",
                default=ARGS["font_margin"],
                type=int,
                dest="font_margin",
            )

        case "font_name":
            parser.add_argument(
                "-fn",
                help="Set up font by given name",
                default=ARGS["font_name"],
                type=str,
                dest="font_name",
            )

        case "font_aliasing":
            parser.add_argument(
                "-fa",
                help="Alias font on render",
                action="store_const",
                const=not ARGS["font_aliasing"],
                default=ARGS["font_aliasing"],
                dest="font_aliasing",
            )

        case "glyph_set":
            parser.add_argument(
                "-g",
                help="List of symbols that will make up the image",
                default=ARGS["glyph_set"],
                type=str,
                dest="glyph_set",
            )

# G color; bg color

        case "image_width":
            parser.add_argument(
                "-w",
                help="List of symbols that will make up the image",
                default=ARGS["image_width"],
                type=int,
                dest="image_width",
            )

        case "image_height":
            parser.add_argument(
                "-h",
                help="List of symbols that will make up the image",
                default=ARGS["image_height"],
                type=int,
                dest="image_height",
            )

def setup(script_name):
    settings = tomllib.load(open("settings.toml", "rb"))
    ARGS = settings[script_name]

    # Parse arguments
    parser = argparse.ArgumentParser(add_help=False)
    add_argument("help", parser, ARGS)

    for argument in ARGS:
        add_argument(argument, parser, ARGS)

    parsed_args = dict(parser.parse_args()._get_kwargs())
    for arg in parsed_args:
        ARGS[arg] = parsed_args[arg]

    # print(ARGS)
    return ARGS
