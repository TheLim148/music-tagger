from music_tagger.cli import create_parser, collect_tag_updates
from music_tagger.tags import print_dump, print_info, preview_changes

current_tags = {
  "title": "Old title",
  "artist": "Old artist",
  "album": "Old album",
  "genre": "Rock"
}

updates = {
  "title": "New title"
}

def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    if args.command == 'info':
        print_info(args.path_to_audio)
    elif args.command == 'dump':
        print_dump(args.path_to_audio)
    elif args.command == 'set':
        updates = collect_tag_updates(args)
        
        if updates is None:
            print("There is no any tag for change")
        else:
            print("updates идёт дальше в tags.py")
            

            preview_changes(current_tags, updates)

    elif args.command == 'scan':
        pass
    else:
        print("...")



if __name__ == "__main__":
    main()
