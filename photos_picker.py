import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, \
    QLineEdit, QTextEdit, QFrame, QStyle, QScrollArea
from PyQt5.QtWidgets import QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt
import os
import shutil

class FolderSelectorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.loading_dialog = None
        self.query_result = None
        self.init_ui()
        self.input_folder = ""
        self.output_folder = ""
        self.customer_query = ""
        self.result_query_list = []
        self.result_query_list_info = []

    def init_ui(self):

        self.setWindowTitle("PHOTOS PICKER")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(400, 200, 400, 150)
        self.resize(600, 400)
        layout = QVBoxLayout()
        # input folder
        self.info_label_input = QLabel("1. Thư mục ảnh INPUT (ảnh gốc):", self)
        self.button_input = QPushButton("Chọn thư mục INPUT", self)
        self.button_input.clicked.connect(self.select_folder_input)
        row_widget = QWidget()
        row_layout = QHBoxLayout()
        row_layout.addWidget(self.info_label_input)
        row_layout.addWidget(self.button_input)
        row_widget.setLayout(row_layout)
        layout.addWidget(row_widget)

        # Thêm line separator
        layout.addWidget(self.new_step())

        # output folder
        self.info_label_output = QLabel("2. Thư mục ảnh OUTPUT (ảnh chọn):", self)
        self.button_output = QPushButton("Chọn thư mục OUTPUT", self)
        self.button_output.clicked.connect(self.select_folder_output)
        row_widget = QWidget()
        row_layout = QHBoxLayout()
        row_layout.addWidget(self.info_label_output)
        row_layout.addWidget(self.button_output)
        row_widget.setLayout(row_layout)
        layout.addWidget(row_widget)

        # Thêm line separator
        layout.addWidget(self.new_step())

        # input query
        self.info_label_query = QLabel("3. Danh sách ảnh cần chọn:", self)
        layout.addWidget(self.info_label_query)

        # Tiền tố
        self.info_label_prefix = QLabel("Tiền tố ảnh:", self)
        self.prefix_input_line = QLineEdit(self)
        self.prefix_input_line.setText("DSCF")
        row_widget = QWidget()
        row_layout = QHBoxLayout()
        row_layout.addWidget(self.info_label_prefix)
        row_layout.addWidget(self.prefix_input_line)
        row_widget.setLayout(row_layout)
        layout.addWidget(row_widget)

        # Hậu tố
        self.info_label_suffix = QLabel("Loại Ảnh:", self)
        self.suffix_radio_raf = QRadioButton("RAF", self)
        self.suffix_radio_jpg = QRadioButton("JPG", self)
        self.suffix_radio_cr3 = QRadioButton("CR3", self)
        self.suffix_radio_nef = QRadioButton("NEF", self)
        self.suffix_radio_raf.setChecked(True)
        self.suffix_button_group = QButtonGroup(self)
        self.suffix_button_group.addButton(self.suffix_radio_raf)
        self.suffix_button_group.addButton(self.suffix_radio_jpg)
        self.suffix_button_group.addButton(self.suffix_radio_cr3)
        self.suffix_button_group.addButton(self.suffix_radio_nef)
        row_widget = QWidget()
        row_layout = QHBoxLayout()
        row_layout.addWidget(self.info_label_suffix)
        row_layout.addWidget(self.suffix_radio_raf)
        row_layout.addWidget(self.suffix_radio_jpg)
        row_layout.addWidget(self.suffix_radio_cr3)
        row_layout.addWidget(self.suffix_radio_nef)
        row_widget.setLayout(row_layout)
        layout.addWidget(row_widget)

        row_widget = QWidget()
        row_layout = QHBoxLayout()
        self.textbox_query = QLabel(self)
        self.textbox_query = QTextEdit(self)
        self.textbox_query.setAcceptRichText(False)
        self.textbox_query.setMinimumHeight(500)
        self.textbox_query.setStyleSheet("font-size: 25px; font-family: Arial;")
        self.textbox_query.setLineWrapMode(QTextEdit.NoWrap)

        self.button_query = QPushButton("Kiểm tra!", self)
        self.button_query.clicked.connect(self.process_query)
        row_layout.addWidget(self.textbox_query)
        row_layout.addWidget(self.button_query)
        row_widget.setLayout(row_layout)
        layout.addWidget(row_widget)

        # input query confirmation text
        self.info_query_result = QLabel(f"Danh sách OUTPUT:", self)
        layout.addWidget(self.info_query_result)
        self.query_result = QLabel("---", self)
        self.query_result.setWordWrap(True)
        # Tạo QScrollArea
        scroll = QScrollArea()
        scroll.setMinimumHeight(350)
        scroll.setWidgetResizable(True)  # Cho phép widget resize theo scroll area
        scroll.setWidget(self.query_result)
        layout.addWidget(scroll)

        # Thêm line separator
        layout.addWidget(self.new_step())

        # Run button
        self.run_button = QPushButton("Tiến hành lọc ảnh!", self)
        self.run_button.setStyleSheet("background-color: #4CAF50; color: blue; font-weight: bold; font-size: 23px; border-radius: 8px; padding: 10px;")
        self.run_button.clicked.connect(self.run)
        layout.addWidget(self.run_button)
        self.run_info = QLabel("", self)
        # layout.addWidget(self.run_info)
        scroll_2 = QScrollArea()
        scroll_2.setMinimumHeight(350)
        scroll_2.setWidgetResizable(True)  # Cho phép widget resize theo scroll area
        scroll_2.setWidget(self.run_info)
        layout.addWidget(scroll_2)

        self.setLayout(layout)

    def select_folder_input(self):
        input_folder = QFileDialog.getExistingDirectory(self, "Chọn thư mục INPUT")
        if input_folder:
            self.info_label_input.setText(f"1. Thư mục INPUT: {input_folder}")
            print("input_folder:", input_folder)
        self.input_folder = input_folder

    def select_folder_output(self):
        output_folder = QFileDialog.getExistingDirectory(self, "Chọn thư mục OUTPUT")
        if output_folder:
            self.info_label_output.setText(f"2. Thư mục OUTPUT: {output_folder}")
            print("output_folder:", output_folder)
        self.output_folder = output_folder

    def process_query(self):
        self.customer_query = self.textbox_query.toPlainText()
        self.result_query_list = []
        self.result_query_list_info = []
        pics_set = set()
        # split by new line
        pics = self.customer_query.split("\n")
        for pic in pics:
            pic = pic.strip()
            if pic:
                pic_name = self.prefix_input_line.text() + pic + "." + ("RAF" if self.suffix_radio_raf.isChecked() else
                                                            "JPG" if self.suffix_radio_jpg.isChecked() else
                                                            "CR3" if self.suffix_radio_cr3.isChecked() else
                                                            "NEF")
                self.result_query_list.append(pic_name)
                if pic_name in pics_set:
                    self.result_query_list_info.append(pic_name + "⚠️ (Ảnh trùng lặp)")
                    continue
                else:
                    pics_set.add(pic_name)
                # check if pic_name exists in input folder
                if os.path.exists(self.input_folder + "/" +  pic_name):
                    self.result_query_list_info.append(pic_name + "🟢　OK")
                else:
                    self.result_query_list_info.append(pic_name + "❌ (Không tìm thấy ảnh)")
        result_str = "\n".join(self.result_query_list_info) + f"\n----\nTổng: {len(self.result_query_list_info)} ảnh"
        self.query_result.setText(str(result_str))

    def run(self):
        self.run_info.setText("")
        self.run_info.setStyleSheet("color: black;")
        if not self.input_folder:
            self.run_info.setText("Vui lòng chọn thư mục INPUT !")
            self.run_info.setStyleSheet("color: red;")
            return
        if not self.output_folder:
            self.run_info.setText("Vui lòng chọn thư mục OUTPUT !")
            self.run_info.setStyleSheet("color: red;")
            return
        if not self.result_query_list:
            self.run_info.setText("Vui lòng nhập danh sách ảnh cần chọn!")
            self.run_info.setStyleSheet("color: red;")
            return
        # appear loading dialog
        self.show_loading()
        layout_loading = QVBoxLayout()
        label_loading = QLabel("Đang tiến hành lọc ảnh... Vui lòng chờ...", self.loading_dialog)
        layout_loading.addWidget(label_loading)
        self.loading_dialog.setLayout(layout_loading)
        self.loading_dialog.show()
        QApplication.processEvents()
        # delete all files in output folder
        for filename in os.listdir(self.output_folder):
            file_path = os.path.join(self.output_folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

        copied_count = 0
        for pic in self.result_query_list:
            src_path = self.input_folder + "/" + pic
            dst_path = self.output_folder + "/" + pic
            if os.path.exists(src_path):
                shutil.copy2(src_path, dst_path)
                copied_count += 1
                self.run_info.setText(self.run_info.text() + f"\nCopied: {pic}")
            else:
                self.run_info.setText(self.run_info.text() + f"\nKhông tìm thấy ảnh: {pic}")
                self.run_info.setStyleSheet("color: red;")
        self.run_info.setText(self.run_info.text() + f"\n ---- \nHoàn thành! Đã sao chép {copied_count} ảnh.")
        self.run_info.setStyleSheet("color: green;")
        # close loading dialog
        self.close_loading()
        # open output folder
        os.startfile(self.output_folder)


    def new_step(self):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)  # horizontal line
        line.setFrameShadow(QFrame.Sunken)  # hiệu ứng lõm
        return line

    def show_loading(self):
        self.loading_dialog = QWidget()
        self.loading_dialog.setWindowTitle("Loading")
        self.loading_dialog.setGeometry(500, 300, 300, 100)
        self.loading_dialog.setWindowModality(Qt.ApplicationModal)
        self.loading_dialog.setWindowFlags(self.loading_dialog.windowFlags() & ~Qt.WindowCloseButtonHint)

    def close_loading(self):
        self.loading_dialog.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("QWidget { font-size: 20px; font-family: Arial; }")
    window = FolderSelectorApp()
    window.show()
    sys.exit(app.exec_())
