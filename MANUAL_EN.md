# Photos Picker - User Manual (English)

Welcome to Photos Picker! This guide will walk you through all features and how to use the application effectively.

## Table of Contents
1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Interface Overview](#interface-overview)
4. [Step-by-Step Guide](#step-by-step-guide)
5. [Features Explained](#features-explained)
6. [Language Settings](#language-settings)
7. [Troubleshooting](#troubleshooting)
8. [Tips & Tricks](#tips--tricks)

---

## Installation

### Windows
1. Download `Photos_Picker_Windows.zip`
2. Extract the ZIP file to any folder
3. Double-click `Photos Picker.exe` to run

### macOS
1. Download `Photos_Picker_macOS.zip`
2. Extract the ZIP file
3. Double-click `Photos Picker.app` to run
4. If you see "App is damaged" error, run in Terminal:
   ```bash
   xattr -d com.apple.quarantine "Photos Picker.app"
   ```

### Linux
1. Download `Photos_Picker_Linux.zip`
2. Extract and run: `./Photos\ Picker`

---

## Quick Start

**In 5 minutes:**

1. ✅ **Select INPUT folder** - where your original photos are stored
2. ✅ **Select OUTPUT folder** - where you want selected photos copied
3. ✅ **Enter photo numbers** - one number per line (e.g., 1234, 5678)
4. ✅ **Click "Check"** - verify which photos exist
5. ✅ **Click "Start"** - copy selected photos to output folder

Done! Your photos are copied.

---

## Interface Overview

### Main Window Layout

```
┌─────────────────────────────────────────────────────────────┐
│  🌐 English                                  [Language Toggle]
├─────────────────────────────────────────────────────────────┤
│ INPUT Folder Section                                         │
│ ├─ Current path or "No folder selected"                     │
│ └─ [📁 Choose INPUT]                                        │
│                                                              │
│ OUTPUT Folder Section                                        │
│ ├─ Current path or "No folder selected"                     │
│ └─ [📁 Choose OUTPUT]                                       │
├─────────────────────────────────────────────────────────────┤
│ Prefix:     [DSCF    ]  Brand: [Fujifilm ▼]  Format: [RAF ▼] │
├─────────────────────────────────────────────────────────────┤
│ LEFT PANEL                   │ RIGHT PANEL                   │
│ Photo number list            │ Results                       │
│ ─────────────────────────    │ ─────────────────────────    │
│ [Text input area]            │ ✔ 10  ✘ 2  ⚠ 1             │
│                              │ [Result list]                │
│ [🔍 Check]                   │                              │
├─────────────────────────────────────────────────────────────┤
│ [▶ Start copying photos]  Progress: 0 / 10 photos           │
│ [═══════════════════════] 50%                               │
│ [Log output area]                                            │
└─────────────────────────────────────────────────────────────┘
```

---

## Step-by-Step Guide

### Step 1: Choose INPUT Folder

The INPUT folder contains your original RAW/JPEG photos.

1. Click **[📁 Choose INPUT]** button
2. Browse and select a folder (e.g., `D:\Customer_Photos\RAW`)
3. The path appears below the button
4. ✅ Folder is now ready for use

**Example folder structure:**
```
D:\Customer_Photos\RAW\
├── DSCF0001.RAF
├── DSCF0002.RAF
├── DSCF0003.RAF
└── ...
```

### Step 2: Choose OUTPUT Folder

The OUTPUT folder is where selected photos will be saved.

1. Click **[📁 Choose OUTPUT]** button
2. Select or create a new folder (e.g., `D:\Customer_Photos\Selected`)
3. The path appears below the button
4. ✅ Folder is ready

**Note:** The folder will be created if it doesn't exist.

### Step 3: Set Photo Parameters

Configure how photos are named:

- **Prefix** - The text at the start of photo names (default: `DSCF`)
  - Example: If prefix is `DSCF` and number is `1234`, app looks for `DSCF1234.RAF`

- **Brand** - Camera brand (Fujifilm, Canon, Nikon, etc.)
  - Determines available file formats

- **Format** - File type (RAF, JPG, CR3, NEF, etc.)
  - Changes based on selected brand

**Common combinations:**
- Fujifilm + RAF
- Canon + CR3 (or CR2)
- Nikon + NEF
- Sony + ARW

### Step 4: Enter Photo Numbers

In the left panel, enter the photo numbers:

1. Click in the **"Photo number list"** text area
2. Enter numbers, **one per line**:
   ```
   1234
   5678
   1001
   999
   ```
3. Or paste from spreadsheet (Excel, Google Sheets)
4. Each line is one photo number

**Tips:**
- Copy from Excel/Sheets and paste directly
- Numbers are trimmed (spaces removed)
- Empty lines are ignored
- Duplicates shown in Results

### Step 5: Check Photos

Verify which photos exist before copying:

1. Click **[🔍 Check]** button
2. App scans the INPUT folder
3. Results appear in right panel:
   - **✔ OK** (green) - Photo found and will be copied
   - **✘ Not Found** (red) - Photo missing, won't be copied
   - **⚠ Duplicate** (orange) - Photo number appears twice

**Example Results:**
```
✔ DSCF1234.RAF    (found)
✔ DSCF5678.RAF    (found)
✘ DSCF1001.RAF    (not found)
⚠ DSCF999.RAF     (duplicate)
```

### Step 6: Start Copying

Copy the selected photos to OUTPUT folder:

1. Review the check results (optional)
2. Click **[▶ Start copying photos]** button
3. Progress bar shows copying status
4. Log shows each file copied
5. When done, OUTPUT folder opens automatically

**Log entries:**
```
✔ Copied: DSCF1234.RAF
✔ Copied: DSCF5678.RAF
✘ Not found: DSCF1001.RAF
✔ Done! Copied 2 photos.
```

---

## Features Explained

### 1. Language Toggle

Switch between Vietnamese and English:

- **Button Location:** Top-right corner
- **Current**: Shows opposite language (e.g., "🌐 Tiếng Việt" when in English)
- **Click to Switch:** All text updates instantly
- **Persistent:** Language preference saved on exit

### 2. Camera Brands & Formats

Supported camera formats by brand:

| Brand | Formats |
|-------|---------|
| Canon | CR3, CR2, CRW, JPG, JPEG |
| Nikon | NEF, NRW, JPG, JPEG |
| Sony | ARW, SR2, SRF, JPG, JPEG |
| Fujifilm | RAF, JPG, JPEG |
| Panasonic | RW2, RWL, JPG, JPEG |
| Olympus | ORF, JPG, JPEG |
| Pentax | PEF, DNG, JPG, JPEG |
| Leica | DNG, RWL, JPG, JPEG |
| Hasselblad | 3FR, FFF, JPG, JPEG |
| GoPro | GPR, JPG, JPEG |
| Phase One | IIQ, JPG, JPEG |
| Red | RED, JPG, JPEG |
| Sigma | X3F, JPG, JPEG |
| Blackmagic | BRAW, JPG, JPEG |

### 3. Duplicate Detection

The app prevents copying the same photo twice:

- **Input** - Enter number `1234` twice
- **Check Result** - One shows ✔ (OK), one shows ⚠ (Duplicate)
- **Copy** - Only one copy is created

### 4. File Preservation

Original metadata is preserved:

- Creation date and time
- EXIF data
- File attributes

Uses `shutil.copy2` (preserves metadata on all platforms).

### 5. Cross-Platform Compatibility

Works on:
- ✅ Windows (7, 10, 11)
- ✅ macOS (10.13+)
- ✅ Linux (Ubuntu, Debian, etc.)

---

## Language Settings

### Switching Languages

**Method 1: Button**
- Click **🌐 English** (when in Vietnamese) or **🌐 Tiếng Việt** (when in English)
- All UI text updates instantly

**Method 2: First Launch**
- On first launch, app uses English
- Switch to Vietnamese with the button
- Setting is saved automatically

### Supported Languages

| Language | Abbreviation |
|----------|--------------|
| English | EN |
| Vietnamese | VI |

### What Gets Translated

✅ All buttons and labels
✅ Error messages
✅ Log output
✅ Dialog titles
✅ Placeholders

**Not translated:**
- Camera brand names (Canon, Nikon, etc.)
- File format codes (RAF, NEF, JPG)

---

## Troubleshooting

### Problem: "Please choose the INPUT folder!"

**Solution:** Click [📁 Choose INPUT] and select a folder containing photos.

### Problem: "Please choose the OUTPUT folder!"

**Solution:** Click [📁 Choose OUTPUT] and select (or create) a destination folder.

### Problem: "Please enter the photo list first!"

**Solution:**
1. Enter photo numbers in the left text area
2. Click [🔍 Check] first
3. Then click [▶ Start copying photos]

### Problem: All photos show "Not found"

**Causes:**
- Wrong prefix (check photo names in INPUT folder)
- Wrong camera brand/format
- Wrong INPUT folder selected

**Solution:**
1. Open INPUT folder and check photo names
2. Adjust prefix to match (e.g., change `DSCF` to `IMG`)
3. Select correct brand and format

### Problem: APP won't open on macOS

**Error:** "App is damaged or can't be opened"

**Solution:**
```bash
xattr -d com.apple.quarantine "Photos Picker.app"
```

Or in System Preferences > Security & Privacy, allow the app.

### Problem: Output folder is empty

**Causes:**
- No photos marked as ✔ OK in Check results
- Copy operation didn't complete

**Solution:**
1. Run Check again
2. Verify results show ✔ OK items
3. Make sure OUTPUT folder is writable
4. Try copying to different location

### Problem: Photo names don't match

**Example:**
- File: `DSCF1234.RAF`
- Entered: `1234`
- Prefix: `DSCF` ✓ Correct
- Format: `RAF` ✓ Correct
- But still shows "Not found"

**Solution:**
- Check for spaces: photo might be `DSCF 1234.RAF` (with space)
- Verify exact file name in INPUT folder
- Copy exact file name from Explorer/Finder

### Problem: Duplicate detection not working

**Example:**
- Enter: `1234`, `1234` (same number twice)
- Both show ✔ OK instead of showing one as duplicate

**Solution:** This shouldn't happen. Try:
1. Click [🔍 Check] again
2. Restart the app
3. Re-enter numbers carefully

---

## Tips & Tricks

### Tip 1: Use Spreadsheet Input

Copy-paste from Excel/Google Sheets:

1. In spreadsheet, select photo number column
2. Copy (Ctrl+C or Cmd+C)
3. In Photos Picker, click text area
4. Paste (Ctrl+V or Cmd+V)

### Tip 2: Save Settings

App remembers:
- Last used folders
- Prefix value
- Selected brand and format
- Language preference

This saves time on next use!

### Tip 3: Check Before Copy

Always click [🔍 Check] before [▶ Start]:
- See which photos will be copied
- Verify numbers are correct
- Avoid copying wrong photos

### Tip 4: Handle Missing Photos

If some photos show ✘ Not found:

**Option 1:** Ask customer for correct numbers
**Option 2:** Check INPUT folder for similar names
**Option 3:** Try different prefix or format

### Tip 5: Batch Operations

To process multiple customers:

1. Copy customer 1 numbers → Check → Copy
2. Empty text area
3. Enter customer 2 numbers → Check → Copy
4. Repeat for each customer

### Tip 6: Find Photos Easily

If you don't know exact numbers:

1. Open INPUT folder
2. Sort by name or date
3. Identify photo names
4. Enter those numbers

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl+A (Cmd+A on Mac) | Select all text in photo list |
| Ctrl+C (Cmd+C) | Copy selected text |
| Ctrl+V (Cmd+V) | Paste photo numbers |

---

## Getting Help

**Still having issues?**

1. Check this manual again (use Ctrl+F to search)
2. Verify INPUT folder path and photo names
3. Try restarting the app
4. Check system requirements (Python 3.8+, 500MB disk space)

---

## System Requirements

- **Windows**: 7 or later, 500MB disk space
- **macOS**: 10.13 or later, 500MB disk space
- **Linux**: Ubuntu 18.04+, 500MB disk space
- **RAM**: 2GB minimum (4GB recommended)
- **Python**: 3.8+ (for development)

---

## Version Information

- **Version**: 1.0.0
- **Last Updated**: March 2026
- **Languages**: English, Vietnamese
- **Platforms**: Windows, macOS, Linux

---

## License

Photos Picker is provided as-is for personal and professional use.

---

**Thank you for using Photos Picker!**

For feedback or suggestions, please let me know.
