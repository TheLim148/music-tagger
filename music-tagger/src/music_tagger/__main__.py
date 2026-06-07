from music_tagger.cli import create_parser, collect_tag_updates
from music_tagger.tags import print_dump, print_info, preview_changes, read_current_tags

def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    if args.command == 'info':
        print_info(args.path_to_audio)
    elif args.command == 'dump':
        print_dump(args.path_to_audio)
    elif args.command == 'set':
        updates = collect_tag_updates(args)
        current_tags = read_current_tags(args.path_to_audio)
        if updates is None:
            print("There is no any tag for change")
        else:
            preview_changes(current_tags, updates)

    elif args.command == 'scan':
        pass
    else:
        print("...")



if __name__ == "__main__":
    main()
