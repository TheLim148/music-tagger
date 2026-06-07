import argparse
from pathlib import Path

SETTABLE_TAGS = [
    "title",
    "artist",
    "album",
    "tracknumber",
    "genre",
]

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
    parser_info.add_argument("path_to_audio", type=Path)

    parser_dump = subparsers.add_parser(
        "dump",
        help="shows all info about track",
    )
    parser_dump.add_argument("path_to_audio", type=Path)

    parser_set = subparsers.add_parser(
        "set",
        help="",
    )
    parser_set.add_argument("path_to_audio", type=Path)
    parser_set.add_argument("--title", type=str)
    parser_set.add_argument("--artist", type=str)
    parser_set.add_argument("--album", type=str)
    parser_set.add_argument("--tracknumber", type=int)
    parser_set.add_argument("--genre", type=str)
    parser_set.add_argument("--dry-run", action="store_true")


    return parser

def collect_tag_updates(args) -> dict[str, str]:
    updates = {}

    for tag_name in SETTABLE_TAGS:
        value = getattr(args, tag_name)

        if value is not None:
            updates[f"{tag_name}"] = value

    return updates