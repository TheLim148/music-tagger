from music_tagger.cli import create_parser, collect_tag_updates
from music_tagger.tags import print_dump, print_info, preview_changes, read_current_tags, set_tags

def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    if args.command == 'info':
        print_info(args.path_to_audio)
    elif args.command == 'dump':
        print_dump(args.path_to_audio)
    elif args.command == 'set':
        updates = collect_tag_updates(args)
        if not bool(updates):
            print("There is no any tag for change")
        else:
            set_tags(args.path_to_audio, updates, args.dry_run)            

    elif args.command == 'scan':
        pass
    else:
        print("...")



if __name__ == "__main__":
    main()
