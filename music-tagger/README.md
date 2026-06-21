# Music Tagger — Usage

## Installation

The project uses [uv](https://docs.astral.sh/uv/).

Install dependencies:

```bash
uv sync
```

## Running

```bash
uv run python -m music_tagger <command> [arguments]
```

Use `--help` to display available commands and arguments:

```bash
uv run python -m music_tagger --help
uv run python -m music_tagger set --help
```

## Commands

### `info`

Display common tags of an MP3 file:

```bash
uv run python -m music_tagger info song.mp3
```

### `dump`

Display all raw ID3 frames:

```bash
uv run python -m music_tagger dump song.mp3
```

### `set`

Change one or more tags:

```bash
uv run python -m music_tagger set song.mp3 \
  --title "Track title" \
  --artist "Artist" \
  --album "Album"
```

Preview changes without modifying the file:

```bash
uv run python -m music_tagger set song.mp3 \
  --title "New title" \
  --dry-run
```

Create a backup before saving:

```bash
uv run python -m music_tagger set song.mp3 \
  --title "New title" \
  --backup
```

### `scan`

Scan a directory for MP3 files and inspect their tags:

```bash
uv run python -m music_tagger scan ~/Music
```

## Supported tags

The application currently works with common fields such as:

* `title`
* `artist`
* `album`
* `albumartist`
* `tracknumber`
* `date`
* `genre`

## Status

The application is minimally functional. Development is temporarily suspended.
