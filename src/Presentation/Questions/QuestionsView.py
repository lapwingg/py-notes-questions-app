from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

from src.Presentation.Questions.QuestionDetailsView import QuestionDetailsView


class QuestionsView(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: green;")
        self.layout = QVBoxLayout()
        self.button = QPushButton('Click me!')
        self.button.clicked.connect(self.__on_button_clicked_event)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def __on_button_clicked_event(self):
        question_details = QuestionDetailsView()
        question_details.setParent(self)
        question_details.setFixedWidth(self.width())
        question_details.setFixedHeight(self.height())
        question_details.show()
