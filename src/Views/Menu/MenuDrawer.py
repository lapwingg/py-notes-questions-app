from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QSizePolicy
import PyQt5.QtCore as QtCore


class MenuDrawer(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: black;")
        policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        policy.setHorizontalStretch(1)
        self.setSizePolicy(policy)