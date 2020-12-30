from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QShowEvent

from src.Database.Database import Database


class QuestionDetailsView(QWidget):
    def __init__(self, question=None):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: blue;")
        self.layout = QVBoxLayout()
        self.button = QPushButton('Back!')
        self.button.clicked.connect(self.__on_button_clicked_event)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        database = Database()
        questions = database.get_questions()
        number = len(questions)
        database.insert_question(f"Question_{number}", "Answer")

    def __on_button_clicked_event(self):
        self.hide()
        self.parent().showEvent(QShowEvent.Show)
