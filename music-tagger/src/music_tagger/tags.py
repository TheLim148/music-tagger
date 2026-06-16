from pathlib import Path
from datetime import datetime
import shutil

from mutagen import File, MutagenError
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, ID3NoHeaderError, APIC

from . import MAIN_TAGS

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

def make_backup(path: Path):
    now = datetime.now()
    timestamp = now.strftime("%d-%m-%Y_%H-%M-%S")
    suffix = ".bak"
    filename = path.name
    new_filename = filename + "." + timestamp + suffix
    new_path = Path(path.parent / new_filename)

    try:
        shutil.copy2(path, new_path)
    except PermissionError:
        print("Permission denied: cannot create a backup")
    except OSError as err:
        print(f"Backup failed {err}")

    return new_path


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

def read_current_tags(path: Path):
    current_tags = {}

    try:
        audio = EasyID3(path)
    except ID3NoHeaderError:
        print("There is no ID3 tags")

    for tag_name, value in audio.items():
        current_tags[f"{tag_name}"] = value
        
    return current_tags

def set_tags(
        path: Path, 
        updates: dict[str, str], 
        dry_run: bool,
        backup: bool,
    ) -> None:

    if not bool(updates):
        print("There is no any tag to update")
        return

    if not path.exists():
        print(f"File not found: {path}")
        return
    
    if not path.is_file():
        print(f"Path is not file: {path}")
        return

    try:
        current_tags = read_current_tags(path)
        has_id3 = True
    except ID3NoHeaderError:
        current_tags = {}
        has_id3 = False
    
    preview_changes(current_tags, updates)

    if dry_run:
        if not has_id3:
            print("ID3 tags would be created")
        print("Dry run: file was not changed")
        return
    
    if backup:
        backup_path = make_backup(path)
        print(f"Backup created: {backup_path}")
    
    if not has_id3:
        audio = File(path, easy=True)
        if audio is None:
            print("Can't define type of audiofile")
            return

        audio.add_tags()

    for tag_name, new_value in updates.items():
        audio[tag_name] = [new_value]

    try:
        audio.save()
    except PermissionError:
        print("Permission denied: cannot save file")
    except OSError as err:
        print(f"File system error while saving file: {err}")