# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for macOS app bundle
# Usage: pyinstaller Photos_Picker_macOS.spec

import os

block_cipher = None

a = Analysis(
    ['photos_picker.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['PyQt5.QtGui', 'PyQt5.QtCore', 'PyQt5.QtWidgets'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib', 'numpy', 'pandas'],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Photos Picker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.icns' if os.path.exists('icon.icns') else None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Photos Picker',
)

app = BUNDLE(
    coll,
    name='Photos Picker.app',
    icon='icon.icns' if os.path.exists('icon.icns') else None,
    bundle_identifier='com.photospicker.app',
    info_plist={
        'NSPrincipalClass': 'NSApplication',
        'NSHighResolutionCapable': 'True',
    },
)
