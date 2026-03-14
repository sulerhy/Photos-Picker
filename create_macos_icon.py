#!/usr/bin/env python3
"""
Convert PNG icon to macOS .icns format.
Requires: Pillow
"""

import subprocess
import sys
import os
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Installing Pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "-q"])
    from PIL import Image

def create_icns_from_png(png_path: str, output_icns: str) -> bool:
    """
    Convert PNG to ICNS using PIL (simple method).
    Note: For best results on macOS, use Image2Icon or iconutil.
    """
    try:
        img = Image.open(png_path).convert('RGBA')

        # Create a temporary directory for icon set
        icon_set_path = Path("Photos Picker.iconset")
        icon_set_path.mkdir(exist_ok=True)

        # Create various sizes required by .icns
        sizes = [
            (16, "16x16"),
            (32, "32x32"),
            (64, "64x64"),
            (128, "128x128"),
            (256, "256x256"),
            (512, "512x512"),
        ]

        for size, name in sizes:
            # Standard resolution
            icon_sized = img.resize((size, size), Image.Resampling.LANCZOS)
            icon_sized.save(icon_set_path / f"icon_{name}.png")

            # Retina resolution (@2x)
            icon_2x = img.resize((size * 2, size * 2), Image.Resampling.LANCZOS)
            icon_2x.save(icon_set_path / f"icon_{name}@2x.png")

        # Try to use iconutil (macOS) or fall back to PIL
        try:
            # This works on macOS with iconutil
            subprocess.run(
                ["iconutil", "-c", "icns", str(icon_set_path), "-o", output_icns],
                check=True,
                capture_output=True
            )
            print(f"[OK] Created {output_icns} using iconutil")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            # Fallback: Save as multi-resolution PNG and document manual conversion
            print("[WARNING] iconutil not found (you're on Windows/Linux)")
            print("  To convert to .icns on macOS, use:")
            print(f"    iconutil -c icns Photos\\ Picker.iconset -o {output_icns}")
            print(f"  Or use online converter: https://convertio.co/png-icns/")
            return False
    except Exception as e:
        print(f"[ERROR] Failed to create .icns: {e}")
        return False

def main():
    png_file = "icon.png"
    icns_file = "icon.icns"

    if not os.path.exists(png_file):
        print(f"[ERROR] {png_file} not found. Run create_icon.py first.")
        sys.exit(1)

    print("Creating macOS icon...")
    success = create_icns_from_png(png_file, icns_file)

    if success:
        print(f"[OK] macOS icon ready: {icns_file}")
    else:
        print(f"[INFO] Icon set created in: Photos Picker.iconset/")
        print(f"  Convert to .icns on macOS or use online tools")

if __name__ == "__main__":
    main()
