from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt


class TechnologiesView(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: yellow;")
