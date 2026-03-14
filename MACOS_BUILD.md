# macOS Build Instructions

This document explains how to build and distribute the Photos Picker app for macOS.

## Prerequisites

- macOS 10.13 or later
- Python 3.8+
- Virtual environment with dependencies installed

## Setup

```bash
# Create/activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install PyQt5 PyInstaller pillow
```

## Building

### Option 1: Using the unified build script (Recommended)

```bash
# Build for current platform (macOS)
python build.py

# Or explicitly:
python build.py --macos
```

Output: `dist/Photos Picker.app`

### Option 2: Manual PyInstaller build

```bash
# First, ensure icon is created (optional but recommended)
python create_macos_icon.py

# Then build with PyInstaller
pyinstaller Photos_Picker_macOS.spec
```

## Icon Setup

The app uses `.icns` format icons on macOS. To create one:

```bash
# Automatic (requires running on macOS with iconutil)
python create_macos_icon.py

# Or manual conversion
# 1. The script creates "Photos Picker.iconset/" directory
# 2. On macOS, run:
iconutil -c icns "Photos Picker.iconset" -o icon.icns
```

For users not on macOS, use an online converter:
- https://convertio.co/png-icns/
- https://icoconvert.com/

## Running the App

After building:

```bash
# Open the app directly
open dist/"Photos Picker.app"

# Or from Finder, double-click the .app bundle
```

## Distribution

### Create a DMG installer (Optional)

```bash
# Simple approach: Just zip the app
zip -r "Photos_Picker_macOS.zip" "dist/Photos Picker.app"

# For a professional DMG installer, use a tool like:
# - Platypus (https://sveinbjorn.org/platypus)
# - create-dmg (npm: npm install -g create-dmg)
```

### Create a zip archive

```bash
cd dist
zip -r ../Photos_Picker_macOS.zip "Photos Picker.app"
```

## Troubleshooting

### "App is damaged or can't be opened"

This usually happens with unsigned apps on macOS. To allow the app to run:

```bash
xattr -d com.apple.quarantine "dist/Photos Picker.app"
```

Or in System Preferences:
1. Go to Security & Privacy
2. Allow "Photos Picker" to run

### PyQt5 not found in built app

This is usually a PyInstaller hook issue. The spec file includes:
```python
hiddenimports=['PyQt5.QtGui', 'PyQt5.QtCore', 'PyQt5.QtWidgets'],
```

If you still get this error, add more Qt modules:
```python
hiddenimports=[
    'PyQt5.QtGui', 'PyQt5.QtCore', 'PyQt5.QtWidgets', 'PyQt5.QtPrintSupport'
],
```

### App doesn't launch from Finder

Try running from terminal to see error:
```bash
open -a "dist/Photos Picker.app" --args
```

Or check the crash log:
```bash
# View system logs
log show --predicate 'eventMessage contains[cd] "Photos Picker"' --last 1h
```

## Code Signing and Notarization (Optional, for distribution)

For public distribution, Apple requires code signing and notarization:

```bash
# Sign the app
codesign --deep --force --verify --verbose --sign "Developer ID Application" \
  "dist/Photos Picker.app"

# Notarize (requires Apple Developer account)
xcrun altool --notarize-app --file Photos_Picker_macOS.zip \
  --primary-bundle-id com.photospicker.app \
  -u <apple_id> -p <app_specific_password>
```

This is only necessary if distributing outside of Mac App Store.

## Cross-Platform Build (from Windows/Linux)

If you want to build the macOS version on Windows:

1. Create icon manually using online converter
2. Run: `pyinstaller Photos_Picker_macOS.spec`
3. Transfer to macOS and code-sign there

Note: Some PyQt5 dependencies are platform-specific, so the resulting .app may have issues if built on non-macOS.

## References

- PyInstaller macOS documentation: https://pyinstaller.org/
- PyQt5 on macOS: https://www.riverbankcomputing.com/software/pyqt/
- Apple code signing: https://developer.apple.com/support/code-signing/
