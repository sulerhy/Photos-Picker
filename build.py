#!/usr/bin/env python3
"""
Cross-platform build script for Photos Picker.
Builds .exe on Windows and .app on macOS.
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def is_windows():
    return sys.platform == "win32"

def is_macos():
    return sys.platform == "darwin"

def is_linux():
    return sys.platform == "linux"

def run_command(cmd, description):
    """Run a command and report progress."""
    print(f"\n[RUN] {description}")
    print(f"      {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, check=True)
        print(f"[OK]  {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {description} failed with code {e.returncode}")
        return False
    except FileNotFoundError as e:
        print(f"[ERROR] Command not found: {e}")
        return False

def check_dependencies():
    """Check if required packages are installed."""
    print("\n[CHECK] Verifying dependencies...")
    required = ["PyQt5", "pyinstaller"]
    for pkg in required:
        try:
            __import__(pkg.lower().replace("-", "_"))
            print(f"  [OK] {pkg}")
        except ImportError:
            print(f"  [MISSING] {pkg}")
            return False
    return True

def create_icon_for_platform():
    """Create platform-specific icon."""
    if is_windows():
        if os.path.exists("icon.ico"):
            print("[OK] Windows icon (icon.ico) already exists")
            return True
        else:
            print("[INFO] Run 'python create_icon.py' to create icon.ico")
            return False

    elif is_macos():
        if os.path.exists("icon.icns"):
            print("[OK] macOS icon (icon.icns) already exists")
            return True
        else:
            print("[INFO] Creating macOS icon...")
            if run_command([sys.executable, "create_macos_icon.py"], "Create macOS icon"):
                return True
            else:
                print("[WARNING] Failed to create .icns, continuing without icon...")
                return True  # Don't fail, just continue

    return True

def build_windows():
    """Build Windows executable."""
    print("\n" + "="*60)
    print("BUILDING WINDOWS EXECUTABLE")
    print("="*60)

    if not create_icon_for_platform():
        print("[WARNING] Icon not found, building without icon...")

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "Photos Picker.spec",
        "--distpath", "dist",
        "--buildpath", "build",
        "--specpath", "."
    ]

    if run_command(cmd, "Build Windows .exe"):
        exe_path = Path("dist/Photos Picker/Photos Picker.exe")
        if exe_path.exists():
            print(f"\n[SUCCESS] Windows build complete!")
            print(f"  Executable: {exe_path}")
            return True
    return False

def build_macos():
    """Build macOS app bundle."""
    print("\n" + "="*60)
    print("BUILDING macOS APP BUNDLE")
    print("="*60)

    if not create_icon_for_platform():
        print("[WARNING] Icon not found, building without icon...")

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "Photos_Picker_macOS.spec",
        "--distpath", "dist",
        "--buildpath", "build",
        "--specpath", "."
    ]

    if run_command(cmd, "Build macOS .app"):
        app_path = Path("dist/Photos Picker.app")
        if app_path.exists():
            print(f"\n[SUCCESS] macOS build complete!")
            print(f"  App bundle: {app_path}")
            print(f"\n  To run: open 'dist/Photos Picker.app'")
            print(f"  To distribute: zip -r 'Photos_Picker_macOS.zip' 'dist/Photos Picker.app/'")
            return True
    return False

def build_linux():
    """Build Linux AppImage/executable."""
    print("\n" + "="*60)
    print("BUILDING LINUX EXECUTABLE")
    print("="*60)

    spec_name = "Photos_Picker_Linux.spec"
    if not os.path.exists(spec_name):
        print(f"[WARNING] {spec_name} not found, creating basic spec...")
        # Just use the Windows spec for now
        spec_name = "Photos Picker.spec"

    cmd = [
        sys.executable, "-m", "PyInstaller",
        spec_name,
        "--distpath", "dist",
        "--buildpath", "build",
        "--specpath", "."
    ]

    if run_command(cmd, "Build Linux executable"):
        exe_path = Path("dist/Photos Picker/Photos Picker")
        if exe_path.exists():
            print(f"\n[SUCCESS] Linux build complete!")
            print(f"  Executable: {exe_path}")
            return True
    return False

def clean_build():
    """Clean build artifacts."""
    print("\n[CLEAN] Removing build artifacts...")
    for path in ["build", "dist", "__pycache__"]:
        if Path(path).exists():
            import shutil
            shutil.rmtree(path)
            print(f"  Removed: {path}")

def main():
    parser = argparse.ArgumentParser(
        description="Build Photos Picker for multiple platforms",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python build.py              # Build for current platform
  python build.py --all        # Build for all platforms
  python build.py --clean      # Clean build artifacts
  python build.py --windows    # Build Windows .exe
  python build.py --macos      # Build macOS .app
        """
    )
    parser.add_argument("--windows", action="store_true", help="Build for Windows")
    parser.add_argument("--macos", action="store_true", help="Build for macOS")
    parser.add_argument("--linux", action="store_true", help="Build for Linux")
    parser.add_argument("--all", action="store_true", help="Build for all platforms")
    parser.add_argument("--clean", action="store_true", help="Clean build artifacts")
    parser.add_argument("--check", action="store_true", help="Check dependencies only")

    args = parser.parse_args()

    print("\n" + "="*60)
    print("PHOTOS PICKER BUILD SYSTEM")
    print("="*60)
    print(f"Platform: {sys.platform}")
    print(f"Python: {sys.version.split()[0]}")

    # Clean if requested
    if args.clean:
        clean_build()
        return

    # Check dependencies
    if not check_dependencies():
        print("\n[ERROR] Missing dependencies. Install with:")
        print("  pip install PyQt5 pyinstaller")
        sys.exit(1)

    if args.check:
        print("\n[OK] All dependencies present")
        return

    # Determine what to build
    build_windows_flag = args.windows or (args.all and is_windows())
    build_macos_flag = args.macos or (args.all and is_macos())
    build_linux_flag = args.linux or (args.all and is_linux())

    # Default to current platform
    if not (args.windows or args.macos or args.linux or args.all):
        if is_windows():
            build_windows_flag = True
        elif is_macos():
            build_macos_flag = True
        else:
            build_linux_flag = True

    # Build
    success = True
    if build_windows_flag:
        success = build_windows() and success
    if build_macos_flag:
        success = build_macos() and success
    if build_linux_flag:
        success = build_linux() and success

    if success:
        print("\n" + "="*60)
        print("ALL BUILDS SUCCESSFUL")
        print("="*60)
    else:
        print("\n[ERROR] Build failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
