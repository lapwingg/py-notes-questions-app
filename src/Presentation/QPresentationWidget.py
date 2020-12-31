from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMessageBox, QHBoxLayout, QVBoxLayout, QLineEdit, QPlainTextEdit
from PyQt5.QtCore import Qt


class QPresentationWidget(QWidget):
    SmallButton = 0
    LargeButton = 1

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: rgba(0, 41, 59, 255)")
        self.layout = self.produce_vertical_layout()

    def set_layout(self):
        self.setLayout(self.layout)

    @staticmethod
    def show_popup_with_text(text):
        alert = QMessageBox()
        alert.setText(text)
        alert.exec_()

    @staticmethod
    def setup_background_color_for_widget(widget):
        widget.setAttribute(Qt.WA_StyledBackground, True)
        widget.setStyleSheet("background-color: white;")

    def produce_button(self, text, size=SmallButton, on_clicked=None, enabled=True):
        button = QPushButton(text)
        if size == self.SmallButton:
            button.setFixedWidth(60)
        elif size == self.LargeButton:
            button.setFixedSize(100, 30)

        self.setup_background_color_for_widget(button)

        if on_clicked:
            button.clicked.connect(on_clicked)

        button.setEnabled(enabled)

        return button

    def produce_label(self, text):
        label = QLabel(text)
        self.setup_background_color_for_widget(label)
        label.setContentsMargins(16, 0, 0, 0)
        return label

    def produce_widget(self, background=False):
        widget = QWidget()

        if background:
            self.setup_background_color_for_widget(widget)

        return widget

    @staticmethod
    def produce_horizontal_layout():
        return QHBoxLayout()

    @staticmethod
    def produce_vertical_layout():
        return QVBoxLayout()

    def produce_line_edit(self, text):
        line_edit = QLineEdit(text)
        self.setup_background_color_for_widget(line_edit)
        return line_edit

    def produce_plain_text_edit(self, plain_text):
        plain_text = QPlainTextEdit(plain_text)
        self.setup_background_color_for_widget(plain_text)
        return plain_text
