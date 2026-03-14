import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from ui.main_window import FolderSelectorApp

if __name__ == "__main__":
    # Enable automatic DPI scaling for 4K and high-resolution monitors
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    app.setStyleSheet("QWidget { font-size: 14px; font-family: Arial; }")
    window = FolderSelectorApp()
    window.show()
    sys.exit(app.exec_())
