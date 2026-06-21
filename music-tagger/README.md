# Music Tagger

A small command-line utility for viewing, editing and checking metadata in MP3 files.

The project is minimally functional. Development is currently frozen.

## Features

- Display common ID3 tags
- Display raw ID3 frames
- Edit common tags
- Preview changes without modifying the file
- Create a backup before writing
- Create ID3 tags for MP3 file that do not have them
- Scan directories for MP3 files
- Report missing or incomplete tags

File renaming and support for additional audio format are not implemented.

## Instalation

```python
uv sync
```

## Usage

```python
uv run python -m music_tagger <command> [arguments]
```

### info

Display common tags of one MP3 file.

```python
uv run python -m music_tagger info song.mp3
```

### dump

Display all raw ID3 frames.

```python
uv run python -m music_tagger dump song.mp3
```

### set

Change one or more tags.

```python
uv run python -m music_tagger set song.mp3 \
  --title "Track title" \
  --artist "Artist" \
  --album "Album"
```

Preview changes without saving:

```python
uv run python -m music_tagger set song.mp3 \
  --title "New title" \
  --dry-run
```

Create a backup before saving:

```python
uv run python -m music_tagger set song.mp3 \
  --title "New title" \
  --backup
```

### scan

Scan a directory for MP3 files and inspect their tags.

```python
uv run python -m music_tagger scan ~/Music
```

Use --help to see all available arguments:

```python
uv run python -m music_tagger --help
uv run python -m music_tagger set --help
```

## Status

Version: `0.9.0`

The application is usable for basic MP3 tag management. Development is temporarily suspended.

## License

See `LICENSE`.