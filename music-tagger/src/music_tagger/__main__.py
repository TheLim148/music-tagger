import argparse
import mutagen
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3

def main():
    parser = argparse.ArgumentParser(description='Some desc')
    subparsers = parser.add_subparsers(dest='command')

    parser_info = subparsers.add_parser('info', help='shows info about track')
    parser_info.add_argument('path_to_audio')

    parser_dump = subparsers.add_parser('dump', help='shows all info about track')
    parser_dump.add_argument('path_to_audio')

    args = parser.parse_args()

    if args.command == 'info':
        audio = EasyID3(args.path_to_audio)
        print(audio)
    elif args.command == 'dump':
        audio = mutagen.File(args.path_to_audio)
        for key, value in audio.items():
            print(f"{key}: {value}")

        print('\n' + '-'*50 + '\n')

        tags_id3 = ID3(args.path_to_audio)
        for tag_name in tags_id3.keys():
            print(f"Tag ID: {tag_name}, Value: {tags_id3[tag_name]}")


if __name__ == "__main__":
    main()
