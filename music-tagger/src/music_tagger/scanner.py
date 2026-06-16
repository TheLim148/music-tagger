from pathlib import Path

from .tags import read_current_tags
from . import MAIN_TAGS

def find_tag_problems(tags: dict[str, str]) -> list[str]:
    problems = []

    if not bool(tags):
        print("Tags are empty")
        return
    
    for tag in MAIN_TAGS:
        values = tags.get(tag)

        if not values:
            problems.append(f"missing {tag}")
    
    return problems

def find_audio_files(path: Path, recursive: bool = False) -> list[Path]:
    audio_files = []

    if recursive:
        pass
    else:
        for file in path.iterdir():
            if file.suffix.lower() == ".mp3":
                audio_files.append(file)

    return audio_files

def scan_directory(
        path: Path, 
        recursive: bool = False, 
        only_problems: bool = False,
    ):

    if not path.exists():
        print(f"Path not found: {path}")
        return

    if not path.is_dir():
        print(f"Path is not directory: {path}")
        return
    
    audio_files = find_audio_files(path)

    for file_path in audio_files:
        tags = read_current_tags(file_path)
        problems = find_tag_problems(tags)

        print(f"file: {file_path.name}")
        for tag in MAIN_TAGS:
            values = tags.get(tag)

            if values:
                print(f"{tag}: {", ".join(values)}")
            else:
                print(f"{tag}: -")

        print(f"problems: {problems if bool(problems) else "-"}\n") 