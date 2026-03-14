from PyQt5.QtCore import QThread, pyqtSignal
from core.service import PhotoPickerService


class CopyWorker(QThread):
    progress = pyqtSignal(str, bool)   # filename, success
    finished = pyqtSignal(int, int)    # copied, skipped
    error    = pyqtSignal(str)

    def __init__(self, filenames: list, input_folder: str, output_folder: str):
        super().__init__()
        self._filenames = filenames
        self._input_folder = input_folder
        self._output_folder = output_folder

    def run(self):
        try:
            copied, skipped = PhotoPickerService.copy_files(
                self._filenames,
                self._input_folder,
                self._output_folder,
                progress_cb=self.progress.emit,
            )
            self.finished.emit(copied, skipped)
        except Exception as exc:
            self.error.emit(str(exc))
