#!/usr/bin/env python3
"""
Create a professional icon for Photos Picker app.
This script creates a PNG icon and converts it to ICO format.
"""

import subprocess
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Installing Pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "-q"])
    from PIL import Image, ImageDraw, ImageFont

def create_icon(size=256):
    """Create a professional Photos Picker icon."""
    # Create a new image with white background
    img = Image.new('RGBA', (size, size), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Color palette from the app
    CLR_HEADER = "#2c3e50"      # Dark blue-gray
    CLR_BTN_CHECK = "#d35400"   # Orange
    CLR_OK = "#27ae60"          # Green
    CLR_PATH_BG = "#ecf0f1"     # Light gray

    # Convert hex to RGB
    header_rgb = tuple(int(CLR_HEADER[i:i+2], 16) for i in (1, 3, 5))
    check_rgb = tuple(int(CLR_BTN_CHECK[i:i+2], 16) for i in (1, 3, 5))
    ok_rgb = tuple(int(CLR_OK[i:i+2], 16) for i in (1, 3, 5))

    # Draw a rounded rectangle background (folder-like shape)
    margin = 20
    draw.rounded_rectangle(
        [(margin, margin), (size - margin, size - margin)],
        radius=30,
        fill=header_rgb,
        outline=None
    )

    # Draw a folder tab at the top
    tab_height = 50
    draw.rounded_rectangle(
        [(margin, margin), (margin + 120, margin + tab_height)],
        radius=15,
        fill=ok_rgb,
        outline=None
    )

    # Draw checkmark (✓) symbol on the folder
    # Using a large filled circle with white checkmark
    check_circle_x = size // 2 + 30
    check_circle_y = size // 2 + 20
    check_radius = 45

    draw.ellipse(
        [(check_circle_x - check_radius, check_circle_y - check_radius),
         (check_circle_x + check_radius, check_circle_y + check_radius)],
        fill=check_rgb,
        outline=None
    )

    # Draw white checkmark using lines (thick strokes to make it visible)
    stroke_width = 8
    # Checkmark path: starts left, goes down-right, then up-right
    # Left part
    draw.line(
        [(check_circle_x - 20, check_circle_y + 5),
         (check_circle_x - 5, check_circle_y + 20)],
        fill='white',
        width=stroke_width
    )
    # Right part
    draw.line(
        [(check_circle_x - 5, check_circle_y + 20),
         (check_circle_x + 25, check_circle_y - 15)],
        fill='white',
        width=stroke_width
    )

    # Draw a small magnifying glass icon in the bottom left corner
    glass_x = margin + 30
    glass_y = size - margin - 30
    glass_radius = 15

    # Magnifying glass circle
    draw.ellipse(
        [(glass_x - glass_radius, glass_y - glass_radius),
         (glass_x + glass_radius, glass_y + glass_radius)],
        outline='white',
        width=3
    )

    # Magnifying glass handle
    draw.line(
        [(glass_x + glass_radius - 5, glass_y + glass_radius - 5),
         (glass_x + glass_radius + 20, glass_y + glass_radius + 20)],
        fill='white',
        width=3
    )

    return img

def main():
    print("Creating Photos Picker icon...")

    # Create icon at different sizes and save as PNG
    icon_png = create_icon(256)
    icon_png.save("icon.png")
    print("[OK] Saved icon.png")

    # Convert PNG to ICO
    try:
        icon_ico = Image.open("icon.png").convert('RGB')
        icon_ico.save("icon.ico", format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32)])
        print("[OK] Saved icon.ico")
    except Exception as e:
        print(f"[ERROR] Error creating ICO: {e}")
        print("  Using PIL's built-in ICO creation...")
        icon_png.convert('RGB').save("icon.ico", format='ICO')
        print("[OK] Saved icon.ico (single size)")

if __name__ == "__main__":
    main()
