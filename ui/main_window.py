from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QFileDialog, QLineEdit, QTextEdit, QFrame, QComboBox, QProgressBar,
)

from core.service import (
    PhotoPickerService, CheckResult,
    DEFAULT_PREFIX, CAMERA_BRANDS,
    STATUS_DUPE, STATUS_MISSING,
)
from core.worker import CopyWorker

# ── Settings ───────────────────────────────────────────────────────────────────
SETTINGS_ORG = "PhotosPicker"
SETTINGS_APP = "PhotosPicker"

# ── Language strings ──────────────────────────────────────────────────────────
STRINGS: dict[str, dict[str, str]] = {
    "vi": {
        "window_title":     "PHOTOS PICKER",
        "lang_button":      "🌐 English",
        "sec_input":        "📁 Thư mục INPUT (ảnh gốc)",
        "sec_output":       "📁 Thư mục OUTPUT (ảnh chọn)",
        "folder_none":      "Chưa chọn thư mục",
        "btn_input":        "📁 Chọn INPUT",
        "btn_output":       "📁 Chọn OUTPUT",
        "dlg_input":        "Chọn thư mục INPUT",
        "dlg_output":       "Chọn thư mục OUTPUT",
        "lbl_prefix":       "Tiền tố ảnh:",
        "lbl_brand":        "Hãng:",
        "lbl_format":       "Định dạng:",
        "sec_query":        "🔍 Danh sách số ảnh",
        "placeholder":      "Nhập số ảnh, mỗi số một dòng...",
        "btn_check":        "🔍 Kiểm tra",
        "sec_results":      "Kết quả",
        "btn_run":          "▶ Tiến hành lọc ảnh",
        "btn_running":      "⏳ Đang xử lý…",
        "err_no_input":     "❌ Vui lòng chọn thư mục INPUT !",
        "err_no_output":    "❌ Vui lòng chọn thư mục OUTPUT !",
        "err_no_list":      "❌ Vui lòng nhập danh sách ảnh cần chọn!",
        "log_copied":       "✔ Đã sao chép: ",
        "log_missing":      "✘ Không tìm thấy: ",
        "log_done":         "✔ Hoàn thành! Đã sao chép {n} ảnh.",
        "log_error":        "❌ Lỗi: ",
        "progress_fmt":     "{done} / {total} ảnh",
    },
    "en": {
        "window_title":     "PHOTOS PICKER",
        "lang_button":      "🌐 Tiếng Việt",
        "sec_input":        "📁 INPUT folder (original photos)",
        "sec_output":       "📁 OUTPUT folder (selected photos)",
        "folder_none":      "No folder selected",
        "btn_input":        "📁 Choose INPUT",
        "btn_output":       "📁 Choose OUTPUT",
        "dlg_input":        "Choose INPUT folder",
        "dlg_output":       "Choose OUTPUT folder",
        "lbl_prefix":       "Prefix:",
        "lbl_brand":        "Brand:",
        "lbl_format":       "Format:",
        "sec_query":        "🔍 Photo number list",
        "placeholder":      "Enter photo numbers, one per line...",
        "btn_check":        "🔍 Check",
        "sec_results":      "Results",
        "btn_run":          "▶ Start copying photos",
        "btn_running":      "⏳ Processing…",
        "err_no_input":     "❌ Please choose the INPUT folder!",
        "err_no_output":    "❌ Please choose the OUTPUT folder!",
        "err_no_list":      "❌ Please enter the photo list first!",
        "log_copied":       "✔ Copied: ",
        "log_missing":      "✘ Not found: ",
        "log_done":         "✔ Done! Copied {n} photos.",
        "log_error":        "❌ Error: ",
        "progress_fmt":     "{done} / {total} photos",
    },
}

# ── Color palette ─────────────────────────────────────────────────────────────
CLR_HEADER    = "#2c3e50"
CLR_BTN_INPUT = "#2980b9"
CLR_BTN_OUT   = "#8e44ad"
CLR_BTN_CHECK = "#d35400"
CLR_BTN_RUN   = "#27ae60"
CLR_OK        = "#27ae60"
CLR_DUPE      = "#e67e22"
CLR_MISSING   = "#e74c3c"
CLR_PATH_BG   = "#f0f0f0"

# ── UI constants ──────────────────────────────────────────────────────────────
WINDOW_GEOMETRY   = (400, 200, 950, 720)
QUERY_BOX_MIN_H   = 160
SCROLL_MIN_H      = 160


def _btn_style(color: str) -> str:
    """Return QSS for a styled button with hover and disabled states."""
    return f"""
        QPushButton {{
            background-color: {color};
            color: white;
            font-weight: bold;
            font-size: 11px;
            border-radius: 6px;
            padding: 8px 16px;
            border: none;
        }}
        QPushButton:hover {{
            background-color: {color}dd;
        }}
        QPushButton:pressed {{
            background-color: {color}99;
        }}
        QPushButton:disabled {{
            background-color: #bdc3c7;
            color: #95a5a6;
        }}
    """


def _section_label(text: str) -> QLabel:
    """Return a bold dark header label."""
    label = QLabel(text)
    label.setStyleSheet(f"color: {CLR_HEADER}; font-weight: bold; font-size: 11px;")
    return label


class FolderSelectorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.input_folder: str = ""
        self.output_folder: str = ""
        self._check_results: list[CheckResult] = []
        self._worker: CopyWorker | None = None
        self._run_log: list[str] = []
        self._copy_total: int = 0
        self._copy_done: int = 0
        self._lang: str = "vi"
        self._init_ui()

    # ── Translation helper ─────────────────────────────────────────────────────

    def _t(self, key: str) -> str:
        return STRINGS[self._lang][key]

    # ── Init UI ───────────────────────────────────────────────────────────────

    def _init_ui(self):
        self.setWindowTitle(self._t("window_title"))
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(*WINDOW_GEOMETRY)
        self.setMinimumSize(800, 600)

        layout = QVBoxLayout()
        layout.setContentsMargins(14, 14, 14, 14)
        layout.setSpacing(8)

        # Language toggle button
        self.lang_button = QPushButton(self._t("lang_button"))
        self.lang_button.setStyleSheet(_btn_style(CLR_HEADER))
        self.lang_button.setMaximumWidth(130)
        self.lang_button.clicked.connect(self._toggle_language)
        lang_row = QHBoxLayout()
        lang_row.addStretch()
        lang_row.addWidget(self.lang_button)
        layout.addLayout(lang_row)

        layout.addWidget(self._init_folder_section())
        layout.addWidget(self._init_query_section())
        layout.addWidget(self._new_separator())
        layout.addWidget(self._init_run_section())
        self.setLayout(layout)
        self._load_settings()

    def _init_folder_section(self) -> QWidget:
        container = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)

        # Input folder
        self.lbl_sec_input = _section_label(self._t("sec_input"))
        layout.addWidget(self.lbl_sec_input)
        self.info_label_input = QLabel(self._t("folder_none"))
        self.info_label_input.setStyleSheet(f"color: #95a5a6; font-style: italic; background-color: {CLR_PATH_BG}; padding: 6px; border-radius: 4px;")
        self.button_input = QPushButton(self._t("btn_input"))
        self.button_input.setStyleSheet(_btn_style(CLR_BTN_INPUT))
        self.button_input.clicked.connect(lambda: self._select_folder(self._t("dlg_input"), self.info_label_input, "input_folder"))
        layout.addWidget(self._make_row(self.info_label_input, self.button_input))

        # Output folder
        self.lbl_sec_output = _section_label(self._t("sec_output"))
        layout.addWidget(self.lbl_sec_output)
        self.info_label_output = QLabel(self._t("folder_none"))
        self.info_label_output.setStyleSheet(f"color: #95a5a6; font-style: italic; background-color: {CLR_PATH_BG}; padding: 6px; border-radius: 4px;")
        self.button_output = QPushButton(self._t("btn_output"))
        self.button_output.setStyleSheet(_btn_style(CLR_BTN_OUT))
        self.button_output.clicked.connect(lambda: self._select_folder(self._t("dlg_output"), self.info_label_output, "output_folder"))
        layout.addWidget(self._make_row(self.info_label_output, self.button_output))

        container.setLayout(layout)
        return container

    def _init_query_section(self) -> QWidget:
        container = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)

        # Prefix + brand + format dropdowns row
        self.lbl_prefix = QLabel(self._t("lbl_prefix"))
        self.prefix_input_line = QLineEdit()
        self.prefix_input_line.setText(DEFAULT_PREFIX)
        self.prefix_input_line.setMaximumWidth(150)
        self.prefix_input_line.textChanged.connect(self._save_settings)

        self.lbl_brand = QLabel(self._t("lbl_brand"))
        self.brand_combo = QComboBox()
        self.brand_combo.addItems(list(CAMERA_BRANDS.keys()))
        self.brand_combo.currentTextChanged.connect(self._on_brand_changed)

        self.lbl_format = QLabel(self._t("lbl_format"))
        self.format_combo = QComboBox()
        self.format_combo.currentTextChanged.connect(self._save_settings)

        # Populate format_combo for initial brand
        self._on_brand_changed(self.brand_combo.currentText())

        prefix_row = [self.lbl_prefix, self.prefix_input_line, self.lbl_brand, self.brand_combo, self.lbl_format, self.format_combo]
        layout.addWidget(self._make_row(*prefix_row))

        # Side-by-side: left = query input, right = results
        splitter_layout = QHBoxLayout()
        splitter_layout.setSpacing(8)

        # Left column: query textbox + check button
        left_container = QWidget()
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(4)
        self.lbl_sec_query = _section_label(self._t("sec_query"))
        left_layout.addWidget(self.lbl_sec_query)
        self.textbox_query = QTextEdit()
        self.textbox_query.setAcceptRichText(False)
        self.textbox_query.setPlaceholderText(self._t("placeholder"))
        self.textbox_query.setMinimumHeight(QUERY_BOX_MIN_H)
        self.textbox_query.setLineWrapMode(QTextEdit.NoWrap)
        left_layout.addWidget(self.textbox_query)

        self.button_query = QPushButton(self._t("btn_check"))
        self.button_query.setStyleSheet(_btn_style(CLR_BTN_CHECK))
        self.button_query.clicked.connect(self._on_check)
        left_layout.addWidget(self.button_query)
        left_container.setLayout(left_layout)

        # Right column: result summary + result details
        right_container = QWidget()
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(4)
        self.lbl_sec_results = _section_label(self._t("sec_results"))
        right_layout.addWidget(self.lbl_sec_results)

        self.result_summary = QLabel("---")
        self.result_summary.setStyleSheet("font-weight: bold; color: #2c3e50;")
        right_layout.addWidget(self.result_summary)

        self.query_result = QTextEdit()
        self.query_result.setReadOnly(True)
        self.query_result.setMinimumHeight(QUERY_BOX_MIN_H)
        self.query_result.setAcceptRichText(True)
        right_layout.addWidget(self.query_result)
        right_container.setLayout(right_layout)

        splitter_layout.addWidget(left_container, 1)
        splitter_layout.addWidget(right_container, 1)
        layout.addLayout(splitter_layout)

        container.setLayout(layout)
        return container

    def _init_run_section(self) -> QWidget:
        container = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)

        # Button row with progress label
        btn_row = QHBoxLayout()
        btn_row.setSpacing(8)
        self.run_button = QPushButton(self._t("btn_run"))
        self.run_button.setStyleSheet(_btn_style(CLR_BTN_RUN))
        self.run_button.clicked.connect(self._on_run)
        btn_row.addWidget(self.run_button)

        self.progress_label = QLabel("")
        self.progress_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.progress_label.setStyleSheet("font-weight: bold; color: #2c3e50;")
        btn_row.addWidget(self.progress_label)
        layout.addLayout(btn_row)

        # Progress bar
        self.copy_progress_bar = QProgressBar()
        self.copy_progress_bar.setValue(0)
        self.copy_progress_bar.setVisible(False)
        self.copy_progress_bar.setTextVisible(False)
        self.copy_progress_bar.setStyleSheet(f"""
            QProgressBar {{
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                background-color: #ecf0f1;
                height: 10px;
            }}
            QProgressBar::chunk {{
                background-color: {CLR_OK};
                border-radius: 3px;
            }}
        """)
        layout.addWidget(self.copy_progress_bar)

        # Log display as monospace QTextEdit
        self.run_info = QTextEdit()
        self.run_info.setReadOnly(True)
        self.run_info.setAcceptRichText(True)
        self.run_info.setMinimumHeight(SCROLL_MIN_H)
        self.run_info.setStyleSheet(f"background-color: #f8f9fa; color: #2c3e50; font-family: 'Courier New', monospace; font-size: 9px; padding: 6px;")
        layout.addWidget(self.run_info)

        container.setLayout(layout)
        return container

    # ── Helpers ───────────────────────────────────────────────────────────────

    @staticmethod
    def _make_row(*widgets) -> QWidget:
        row = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        for w in widgets:
            layout.addWidget(w)
        row.setLayout(layout)
        return row

    @staticmethod
    def _new_separator() -> QFrame:
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        return line

    def _select_folder(self, title: str, label: QLabel, attr: str):
        folder = QFileDialog.getExistingDirectory(self, title)
        if folder:
            label.setText(folder)
            label.setStyleSheet(f"color: {CLR_OK}; font-style: normal; background-color: {CLR_PATH_BG}; padding: 6px; border-radius: 4px;")
            setattr(self, attr, folder)

    def _selected_file_type(self) -> str:
        return self.format_combo.currentText()

    def _on_brand_changed(self, brand: str):
        self.format_combo.blockSignals(True)
        self.format_combo.clear()
        self.format_combo.addItems(CAMERA_BRANDS.get(brand, []))
        self.format_combo.blockSignals(False)
        self._save_settings()

    def _save_settings(self):
        s = QSettings(SETTINGS_ORG, SETTINGS_APP)
        s.setValue("language", self._lang)
        s.setValue("prefix", self.prefix_input_line.text())
        s.setValue("brand", self.brand_combo.currentText())
        s.setValue("format", self.format_combo.currentText())

    def _load_settings(self):
        s = QSettings(SETTINGS_ORG, SETTINGS_APP)
        lang = s.value("language", "vi")
        if lang in STRINGS:
            self._lang = lang

        prefix = s.value("prefix", DEFAULT_PREFIX)
        brand = s.value("brand", list(CAMERA_BRANDS.keys())[0])
        fmt = s.value("format", CAMERA_BRANDS[list(CAMERA_BRANDS.keys())[0]][0])

        self.prefix_input_line.setText(prefix)

        idx = self.brand_combo.findText(brand)
        self.brand_combo.setCurrentIndex(idx if idx >= 0 else 0)
        # _on_brand_changed fires here, populating format_combo

        idx = self.format_combo.findText(fmt)
        if idx >= 0:
            self.format_combo.setCurrentIndex(idx)

        self._retranslate_ui()

    # ── Slots ─────────────────────────────────────────────────────────────────

    def _on_check(self):
        numbers = self.textbox_query.toPlainText().split("\n")
        prefix = self.prefix_input_line.text()
        file_type = self._selected_file_type()
        self._check_results = PhotoPickerService.check_files(
            numbers, prefix, file_type, self.input_folder
        )

        # Count results by status
        count_ok = sum(1 for r in self._check_results if r.is_ok)
        count_dupe = sum(1 for r in self._check_results if r.status == STATUS_DUPE)
        count_missing = sum(1 for r in self._check_results if r.status == STATUS_MISSING)

        # Build HTML result lines
        html_lines = []
        for r in self._check_results:
            if r.is_ok:
                color = CLR_OK
                icon = "✔"
            elif r.status == STATUS_DUPE:
                color = CLR_DUPE
                icon = "⚠"
            else:  # STATUS_MISSING
                color = CLR_MISSING
                icon = "✘"
            html_lines.append(f"<span style='color: {color};'>{icon} {r.filename}</span>")

        self.query_result.setHtml("<br>".join(html_lines))

        # Summary with counts
        summary = f"<span style='color: {CLR_OK};'>✔ {count_ok}</span> &nbsp; "
        summary += f"<span style='color: {CLR_MISSING};'>✘ {count_missing}</span> &nbsp; "
        summary += f"<span style='color: {CLR_DUPE};'>⚠ {count_dupe}</span>"
        self.result_summary.setText(summary)

    def _on_run(self):
        self.run_info.setHtml("")

        if not self.input_folder:
            self.run_info.setHtml(f"<span style='color: red;'>{self._t('err_no_input')}</span>")
            return
        if not self.output_folder:
            self.run_info.setHtml(f"<span style='color: red;'>{self._t('err_no_output')}</span>")
            return
        if not self._check_results:
            self.run_info.setHtml(f"<span style='color: red;'>{self._t('err_no_list')}</span>")
            return

        filenames = [r.filename for r in self._check_results if r.is_ok]
        self._run_log = []
        self._copy_total = len(filenames)
        self._copy_done = 0
        self.copy_progress_bar.setValue(0)
        self.copy_progress_bar.setMaximum(self._copy_total if self._copy_total > 0 else 1)
        self.copy_progress_bar.setVisible(True)
        self.progress_label.setText(self._t("progress_fmt").format(done=0, total=self._copy_total))

        # Disable button during processing
        self.run_button.setEnabled(False)
        self.run_button.setText(self._t("btn_running"))

        self._worker = CopyWorker(filenames, self.input_folder, self.output_folder)
        self._worker.progress.connect(self._on_copy_progress)
        self._worker.finished.connect(self._on_copy_finished)
        self._worker.error.connect(self._on_copy_error)
        self._worker.start()

    def _on_copy_progress(self, filename: str, success: bool):
        if success:
            self._run_log.append(f"<span style='color: {CLR_OK};'>{self._t('log_copied')}{filename}</span>")
        else:
            self._run_log.append(f"<span style='color: {CLR_MISSING};'>{self._t('log_missing')}{filename}</span>")
        self._copy_done += 1
        self.copy_progress_bar.setValue(self._copy_done)
        self.progress_label.setText(self._t("progress_fmt").format(done=self._copy_done, total=self._copy_total))

        # Update log with HTML and auto-scroll to bottom
        self.run_info.setHtml("<br>".join(self._run_log))
        self.run_info.verticalScrollBar().setValue(self.run_info.verticalScrollBar().maximum())

    def _on_copy_finished(self, copied: int, skipped: int):
        summary_color = CLR_DUPE if skipped > 0 else CLR_OK
        done_text = self._t("log_done").format(n=copied)
        summary_text = f"<br><br><span style='color: {summary_color}; font-weight: bold;'>{done_text}</span>"
        self._run_log.append(summary_text)
        self.run_info.setHtml("<br>".join(self._run_log))
        self.copy_progress_bar.setVisible(False)
        self.progress_label.setText("")

        # Re-enable button
        self.run_button.setEnabled(True)
        self.run_button.setText(self._t("btn_run"))

        PhotoPickerService.open_folder(self.output_folder)

    def _on_copy_error(self, message: str):
        self._run_log.append(f"<span style='color: {CLR_MISSING}; font-weight: bold;'>{self._t('log_error')}{message}</span>")
        self.run_info.setHtml("<br>".join(self._run_log))
        self.copy_progress_bar.setVisible(False)
        self.progress_label.setText("")

        # Re-enable button
        self.run_button.setEnabled(True)
        self.run_button.setText(self._t("btn_run"))

    def _retranslate_ui(self):
        self.setWindowTitle(self._t("window_title"))
        self.lang_button.setText(self._t("lang_button"))

        self.lbl_sec_input.setText(self._t("sec_input"))
        self.lbl_sec_output.setText(self._t("sec_output"))
        # Only update folder labels if no folder is selected (don't overwrite a path)
        if not self.input_folder:
            self.info_label_input.setText(self._t("folder_none"))
        if not self.output_folder:
            self.info_label_output.setText(self._t("folder_none"))
        self.button_input.setText(self._t("btn_input"))
        self.button_output.setText(self._t("btn_output"))

        self.lbl_prefix.setText(self._t("lbl_prefix"))
        self.lbl_brand.setText(self._t("lbl_brand"))
        self.lbl_format.setText(self._t("lbl_format"))
        self.lbl_sec_query.setText(self._t("sec_query"))
        self.textbox_query.setPlaceholderText(self._t("placeholder"))
        self.button_query.setText(self._t("btn_check"))
        self.lbl_sec_results.setText(self._t("sec_results"))

        if not self.run_button.text() == self._t("btn_running"):
            # Don't overwrite "Processing…" while a run is in progress
            self.run_button.setText(self._t("btn_run"))

    def _toggle_language(self):
        self._lang = "en" if self._lang == "vi" else "vi"
        self._retranslate_ui()
        self._save_settings()

