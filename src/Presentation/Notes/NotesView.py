from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

from src.Presentation.Notes.NoteDetailsView import NoteDetailsView


class NotesView(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: red;")
        self.layout = QVBoxLayout()
        self.button = QPushButton('Click me!')
        self.button.clicked.connect(self.__on_button_clicked_event)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def __on_button_clicked_event(self):
        note_details = NoteDetailsView()
        note_details.setParent(self)
        note_details.setFixedWidth(self.width())
        note_details.setFixedHeight(self.height())
        note_details.show()
