from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

from src.Presentation.Technologies.TechnologyDetailsView import TechnologyDetailsView


class TechnologiesView(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: yellow;")
        self.layout = QVBoxLayout()
        self.button = QPushButton('Click me!')
        self.button.clicked.connect(self.__on_button_clicked_event)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def __on_button_clicked_event(self):
        technology_details = TechnologyDetailsView()
        technology_details.setParent(self)
        technology_details.setFixedWidth(self.width())
        technology_details.setFixedHeight(self.height())
        technology_details.show()
