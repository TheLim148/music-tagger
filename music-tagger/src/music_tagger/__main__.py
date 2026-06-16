from .cli import create_parser, collect_tag_updates
from .tags import print_dump, print_info, set_tags
from .scanner import scan_directory


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
            set_tags(args.path_to_audio, updates, args.dry_run, args.backup)            

    elif args.command == 'scan':
        scan_directory(args.directory)

    else:
        print("...")



if __name__ == "__main__":
    main()
