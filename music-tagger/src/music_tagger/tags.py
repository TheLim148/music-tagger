from pathlib import Path

from mutagen import File, MutagenError
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, ID3NoHeaderError, APIC

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

    try:
        tags_id3 = ID3(path)
    except ID3NoHeaderError:
        print("There is no ID3 tags")
        return
    except MutagenError as e:
        print(f"File read error: {e}")
        return

    print("=== Raw ID3 dump ===")

    for tag_name, value in tags_id3.items():
        if tag_name.startswith('APIC') or isinstance(value, APIC):
            print(f"{tag_name}: +")
        else:
            print(f"{tag_name}: {value}")

def preview_changes(
        current_tags: dict[str, str], 
        updates: dict[str, str]
    ) -> None:

    for tag_name, new_value in updates.items():
        if current_tags.get(tag_name):
            old_value = current_tags.get(tag_name)
        else:
            old_value = "-"
        
        print(f"{tag_name}:\n  old: {old_value} -> new: {new_value}\n")

def read_current_tags(audio: EasyID3):
    current_tags = {}
     
    for tag_name, value in audio.items():
        current_tags[f"{tag_name}"] = value
        
    return current_tags

def set_tags(
        path: Path, 
        updates: dict[str, str], 
        dry_run: bool
    ) -> None:

    audio = EasyID3(path)
    current_tags = read_current_tags(audio)

    if not bool(updates):
        print("There is no any tag to update")
        return
    
    preview_changes(current_tags, updates)

    if dry_run:
        print("Dry run: file was not changed")
    else:
        for tag_name, new_value in updates.items():
            audio[tag_name] = [new_value]

        audio.save()