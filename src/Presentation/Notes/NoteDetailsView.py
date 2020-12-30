from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QShowEvent

from src.Database.Database import Database


class NoteDetailsView(QWidget):
    def __init__(self, note=None):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: orange;")
        self.layout = QVBoxLayout()
        self.button = QPushButton('Back!')
        self.button.clicked.connect(self.__on_button_clicked_event)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        database = Database()
        notes = database.get_notes()
        number = len(notes)
        database.insert_note(f"Note_{number}", "Descpritions")

    def __on_button_clicked_event(self):
        self.hide()
        self.parent().showEvent(QShowEvent.Show)
