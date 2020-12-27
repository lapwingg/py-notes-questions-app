from PyQt5.QtWidgets import QWidget, QSizePolicy
from PyQt5.QtCore import Qt


class PresentationArea(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: red')
        policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        policy.setHorizontalStretch(5)
        self.setSizePolicy(policy)
