# Photos Picker - Export Guide (Windows & macOS)

This guide explains how to build and export the Photos Picker app for different platforms.

## Quick Start

### On Windows

```bash
# Activate environment
venv\Scripts\activate

# Build .exe
python build.py

# Output: dist\Photos Picker\Photos Picker.exe
```

### On macOS

```bash
# Activate environment
source venv/bin/activate

# Build .app
python build.py

# Output: dist/Photos Picker.app
```

## What's New

### Build System
- ✅ **build.py** - Unified cross-platform build script
- ✅ **Photos_Picker_macOS.spec** - macOS app bundle configuration
- ✅ **create_macos_icon.py** - Icon conversion for macOS (.icns format)

### Features
- ✅ **Language Toggle** - Switch between Vietnamese & English
- ✅ **Settings Persistence** - Language preference saved via QSettings
- ✅ **Professional Icon** - Folder + checkmark + magnifying glass design
- ✅ **Cross-Platform** - Works on Windows, macOS, and Linux

## Build Details

### Windows Build

```bash
python build.py --windows
```

Creates:
- `dist/Photos Picker/Photos Picker.exe` - Main executable
- Supporting libraries in `dist/Photos Picker/`

Distributes as `.zip` or installer

### macOS Build

```bash
python build.py --macos
```

Creates:
- `dist/Photos Picker.app` - macOS app bundle
- Includes all dependencies inside the bundle

Distributes as `.zip` or `.dmg` installer

### Icon Setup

The build system automatically uses:
- **Windows**: `icon.ico` (created by `create_icon.py`)
- **macOS**: `icon.icns` (created by `create_macos_icon.py`)

If icons don't exist, builds complete but without custom icon.

## Distribution

### For Windows Users
```bash
# Option 1: Portable ZIP
cd dist
zip -r "Photos_Picker_Windows.zip" "Photos Picker/"

# Option 2: Create installer (requires NSIS)
# ... (advanced, not covered here)
```

### For macOS Users
```bash
# Option 1: Simple ZIP
cd dist
zip -r "Photos_Picker_macOS.zip" "Photos Picker.app"

# Option 2: Professional DMG installer
# Use create-dmg or other DMG tools
```

## File Structure

```
Photos-Picker/
├── build.py                          # Unified build script
├── create_icon.py                    # Windows icon generator
├── create_macos_icon.py              # macOS icon generator
├── Photos Picker.spec                # Windows PyInstaller spec
├── Photos_Picker_macOS.spec          # macOS PyInstaller spec
├── photos_picker.py                  # Main entry point
├── icon.ico                          # Windows icon
├── icon.icns                         # macOS icon (optional)
├── icon.png                          # Source PNG icon
├── CLAUDE.md                         # Developer guide
├── MACOS_BUILD.md                    # Detailed macOS instructions
├── EXPORT_GUIDE.md                   # This file
├── core/
│   ├── service.py                    # Core logic (cross-platform)
│   └── worker.py                     # Threading for file ops
└── ui/
    └── main_window.py                # UI with language support
```

## Key Changes Made

### 1. Language Support
- Added STRINGS dictionary with Vietnamese/English translations
- Language toggle button in top-right corner
- Preference saved in QSettings
- Automatic retranslation of all UI elements

### 2. Icon Design
- Professional folder + checkmark + magnifying glass design
- Multiple formats: PNG, ICO (Windows), ICNS (macOS)
- Color scheme matches app UI

### 3. Build System
- Single `build.py` script for all platforms
- Dependency checking
- Clean command for removing artifacts
- Detailed error reporting

### 4. Cross-Platform Code
- `core/service.py` already supports Windows, macOS, Linux
- `os.startfile()` for Windows
- `subprocess.Popen(["open", path])` for macOS
- `xdg-open` for Linux

## Troubleshooting

### Build fails with "PyQt5 not found"
```bash
pip install PyQt5 pyinstaller
```

### Icon not included in build
```bash
# Windows
python create_icon.py

# macOS
python create_macos_icon.py
```

### macOS app won't run (Gatekeeper error)
```bash
xattr -d com.apple.quarantine "dist/Photos Picker.app"
```

### App runs from terminal but not from Finder (macOS)
Check for missing dependencies:
```bash
# Run with debugging
DYLD_PRINT_LIBRARIES=1 open -a "dist/Photos Picker.app"
```

## Next Steps

### For Distribution
1. ✅ Build the app (`python build.py`)
2. ✅ Test thoroughly on target platform
3. ✅ Create distribution package (.zip or installer)
4. ✅ Test extracted/installed version
5. Share with users

### For Code Signing (macOS distribution)
If distributing to many users:
1. Obtain Apple Developer Certificate
2. Code-sign the app: `codesign --deep --sign "Developer ID"...`
3. Consider notarization for Gatekeeper

See `MACOS_BUILD.md` for detailed code signing instructions.

## References

- **PyInstaller**: https://pyinstaller.org/
- **PyQt5**: https://www.riverbankcomputing.com/software/pyqt/
- **macOS Code Signing**: https://developer.apple.com/support/code-signing/
- **Cross-platform Python**: https://docs.python.org/3/library/sys.html#sys.platform

## Tips

- Test the built app before distribution
- Keep the source icon.png for future modifications
- Use version control for the spec files
- Test on multiple versions of the target OS if possible
- Include release notes when distributing

---

**Created**: March 2026
**Platform Support**: Windows, macOS, Linux
**Language Support**: Vietnamese, English
