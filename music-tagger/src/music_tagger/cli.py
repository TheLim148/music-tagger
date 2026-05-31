import argparse
from pathlib import Path

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="CLI utility for view music tags"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    parser_info = subparsers.add_parser(
        "info",
        help="shows main info about track",
    )
    parser_info.add_argument('path_to_audio', type=Path)

    parser_dump = subparsers.add_parser(
        "dump",
        help="shows all info about track",
    )
    parser_dump.add_argument('path_to_audio', type=Path)

    return parser