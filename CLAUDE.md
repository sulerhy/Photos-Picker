# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This App Does

Photos Picker is a PyQt5 desktop GUI tool for photographers. Given a folder of RAW/JPEG photo files and a customer's list of photo numbers, it constructs full filenames, checks which exist, and copies them to an output folder. The UI supports Vietnamese and English.

## Running and Building

### Development

```bash
# Activate venv and run
source venv/Scripts/activate   # Windows Git Bash
python photos_picker.py
```

### Building (Cross-Platform)

```bash
# Using unified build script (Recommended)
python build.py              # Build for current platform
python build.py --all        # Build for Windows + macOS + Linux
python build.py --windows    # Build Windows .exe
python build.py --macos      # Build macOS .app
python build.py --clean      # Clean build artifacts

# Manual builds
pyinstaller "Photos Picker.spec"          # Windows
pyinstaller Photos_Picker_macOS.spec      # macOS
```

### Icon Generation

```bash
# Create Windows icon (ICO)
python create_icon.py

# Create macOS icon (ICNS)
python create_macos_icon.py
```

See `MACOS_BUILD.md` for detailed macOS build instructions.

## Architecture

Main components:
- `photos_picker.py` — Entry point, sets up QApplication and FolderSelectorApp
- `ui/main_window.py` — UI class with language support (Vietnamese/English)
- `core/service.py` — Photo picker logic and cross-platform folder opening
- `core/worker.py` — Threading for file copy operations

**Core workflow:**
1. User selects input folder (RAW/JPEG files) and output folder
2. Enters photo numbers, prefix, and file type via dropdowns
3. "Check" → validates existence, flags duplicates
4. "Start" → copies matched files via `shutil.copy2`, opens output folder

**Key features:**
- Cross-platform support (Windows, macOS, Linux)
- Bilingual UI (Vietnamese/English) with QSettings persistence
- Professional icon design
- Thread-safe file operations

## Virtual Environments

Two venvs exist:
- `venv/` — primary: PyQt5 + PyInstaller (use for running and building)
- `.venv/` — secondary: PyQt5 + Pillow (use only for `util_icon_converter.py`)
