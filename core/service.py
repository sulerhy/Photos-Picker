import os
import shutil
import subprocess
import sys
from dataclasses import dataclass

DEFAULT_PREFIX = "DSCF"

CAMERA_BRANDS: dict[str, list[str]] = {
    "Canon":        ["CR3", "CR2", "CRW", "JPG", "JPEG"],
    "Nikon":        ["NEF", "NRW", "JPG", "JPEG"],
    "Sony":         ["ARW", "SR2", "SRF", "JPG", "JPEG"],
    "Fujifilm":     ["RAF", "JPG", "JPEG"],
    "Panasonic":    ["RW2", "RWL", "JPG", "JPEG"],
    "Olympus":      ["ORF", "JPG", "JPEG"],
    "Pentax":       ["PEF", "DNG", "JPG", "JPEG"],
    "Leica":        ["DNG", "RWL", "JPG", "JPEG"],
    "Hasselblad":   ["3FR", "FFF", "JPG", "JPEG"],
    "GoPro":        ["GPR", "JPG", "JPEG"],
    "Phase One":    ["IIQ", "JPG", "JPEG"],
    "Red":          ["RED", "JPG", "JPEG"],
    "Sigma":        ["X3F", "JPG", "JPEG"],
    "Blackmagic":   ["BRAW", "JPG", "JPEG"],
}

# Keep flat FILE_TYPES for fallback (first format per brand)
FILE_TYPES = [formats[0] for formats in CAMERA_BRANDS.values()]

STATUS_OK      = "🟢 OK"
STATUS_DUPE    = "⚠️ (Ảnh trùng lặp)"
STATUS_MISSING = "❌ (Không tìm thấy ảnh)"


@dataclass
class CheckResult:
    filename: str
    status: str
    is_ok: bool


class PhotoPickerService:

    @staticmethod
    def build_filename(prefix: str, number: str, file_type: str) -> str:
        return f"{prefix}{number}.{file_type}"

    @staticmethod
    def check_files(
        numbers: list[str],
        prefix: str,
        file_type: str,
        input_folder: str,
    ) -> list[CheckResult]:
        results: list[CheckResult] = []
        seen: set[str] = set()
        for number in numbers:
            number = number.strip()
            if not number:
                continue
            filename = PhotoPickerService.build_filename(prefix, number, file_type)
            if filename in seen:
                results.append(CheckResult(filename=filename, status=STATUS_DUPE, is_ok=False))
                continue
            seen.add(filename)
            path = os.path.join(input_folder, filename)
            if os.path.exists(path):
                results.append(CheckResult(filename=filename, status=STATUS_OK, is_ok=True))
            else:
                results.append(CheckResult(filename=filename, status=STATUS_MISSING, is_ok=False))
        return results

    @staticmethod
    def copy_files(
        filenames: list[str],
        input_folder: str,
        output_folder: str,
        progress_cb,
    ) -> tuple[int, int]:
        copied = 0
        skipped = 0
        for filename in filenames:
            src = os.path.join(input_folder, filename)
            dst = os.path.join(output_folder, filename)
            if os.path.exists(src):
                shutil.copy2(src, dst)
                copied += 1
                progress_cb(filename, True)
            else:
                skipped += 1
                progress_cb(filename, False)
        return copied, skipped

    @staticmethod
    def open_folder(path: str) -> None:
        if sys.platform == "win32":
            os.startfile(path)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])
