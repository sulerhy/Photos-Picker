# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This App Does

Photos Picker is a PyQt5 desktop GUI tool for photographers. Given a folder of RAW/JPEG photo files and a customer's list of photo numbers, it constructs full filenames, checks which exist, and copies them to an output folder. The UI is in Vietnamese.

## Running and Building

```bash
# Run in development
source venv/Scripts/activate   # Windows Git Bash
python photos_picker.py

# Build standalone .exe (output: dist/Photos Picker.exe)
pyinstaller "Photos Picker.spec"

# Or build from scratch
pyinstaller --onefile --noconsole --name="Photos Picker" --icon=icon.ico photos_picker.py

# Convert icon.png to icon.ico (requires .venv with Pillow)
source .venv/Scripts/activate
python util_icon_converter.py
```

No linting or test suite exists.

## Architecture

Everything lives in `photos_picker.py` (single file, ~249 lines). One class: `FolderSelectorApp(QWidget)`.

**Core workflow:**
1. User selects input folder (contains files like `DSCF1234.RAF`) and output folder
2. User enters photo numbers (one per line), a prefix (default `DSCF`), and file type (RAF/JPG/CR3/NEF via radio buttons)
3. "Kiem tra" (Check) → `process_query()` — constructs filenames, checks existence, flags duplicates, shows status list
4. "Tien hanh loc anh" (Proceed) → `run()` — copies matched files via `shutil.copy2`, then opens output folder with `os.startfile()`

**Key instance state:** `input_folder`, `output_folder`, `customer_query` (raw text), `result_query_list` (constructed filenames), `result_query_list_info` (display strings with status).

## Virtual Environments

Two venvs exist:
- `venv/` — primary: PyQt5 + PyInstaller (use for running and building)
- `.venv/` — secondary: PyQt5 + Pillow (use only for `util_icon_converter.py`)
