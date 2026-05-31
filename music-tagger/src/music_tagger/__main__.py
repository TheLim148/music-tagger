from music_tagger.cli import create_parser
from music_tagger.tags import print_dump, print_info


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    if args.command == 'info':
        print_info(args.path_to_audio)
    elif args.command == 'dump':
        print_dump(args.path_to_audio)


if __name__ == "__main__":
    main()
