from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class NoteDetailsView(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: orange;")
        self.layout = QVBoxLayout()
        self.button = QPushButton('Back!')
        self.button.clicked.connect(self.__on_button_clicked_event)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def __on_button_clicked_event(self):
        self.hide()
