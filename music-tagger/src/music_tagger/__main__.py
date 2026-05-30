import argparse
from pathlib import Path

from mutagen import File, MutagenError
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, ID3NoHeaderError

MAIN_TAGS = [
    "title",
    "artist",
    "album",
    "albumartist",
    "tracknumber",
    "date",
    "genre",
]

def print_info(path: Path) -> None:
    try:
        audio = EasyID3(path)
    except ID3NoHeaderError:
        print("There is no ID3 tags")
        return
    except MutagenError as e:
        print(f"File read error: {e}")
        return
    
    print("=== Main tags ===")

    for tag in MAIN_TAGS:
        values = audio.get(tag)

        if values:
            print(f"{tag}: {', '.join(values)}")
        else:
            print(f"{tag}: -")


def print_dump(path: Path) -> None:
    audio = File(path)

    if audio is None:
        print("Can't define a type of audiofile")
        return

    print("=== Raw ID3 dump ===")

    try:
        tags_id3 = ID3(path)
    except ID3NoHeaderError:
        print("There is no ID3 tags")
        return
    except MutagenError as e:
        print(f"File read error: {e}")
        return

    for tag_name, value in tags_id3.items():
        print(f"{tag_name}: {value}")



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


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    if args.command == 'info':
        print_info(args.path_to_audio)
    elif args.command == 'dump':
        print_dump(args.path_to_audio)


if __name__ == "__main__":
    main()
