from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QLineEdit, QPlainTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QShowEvent

from src.Database.Database import Database


class QuestionDetailsView(QWidget):
    question_name = ""
    question_answer = ""
    question = None

    def __init__(self, question=None):
        super().__init__()
        if question:
            self.question = question
            self.question_name = self.question.question
            self.question_answer = self.question.answer

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: rgba(0, 41, 59, 255)")
        self.layout = QVBoxLayout()
        self.__setup_top_bar_buttons()
        self.__setup_edit_question_layout()
        self.setLayout(self.layout)

    def __setup_top_bar_buttons(self):
        top_bar_layout = QHBoxLayout()
        widget = QWidget()
        show_answer_button = self.__setup_button('Answer')
        show_answer_button.clicked.connect(self.__on_show_answer_clicked)
        back_button = self.__setup_button('Back')
        back_button.clicked.connect(self.__on_back_button_clicked)
        self.save_button = self.__setup_button('Save')
        self.save_button.clicked.connect(self.__on_save_button_clicked)
        top_bar_layout.addWidget(widget)
        top_bar_layout.addWidget(show_answer_button)
        top_bar_layout.addWidget(back_button)
        top_bar_layout.addWidget(self.save_button)

        if self.question:
            self.save_button.setEnabled(False)
        else:
            show_answer_button.setEnabled(False)

        self.layout.addLayout(top_bar_layout)

    def __on_show_answer_clicked(self):
        self.save_button.setEnabled(True)
        self.edit_answer.setEnabled(True)
        self.edit_answer.setPlainText(self.question_answer)

    def __on_back_button_clicked(self):
        self.hide()
        self.parent().showEvent(QShowEvent.Show)

    def __on_save_button_clicked(self):
        database = Database()
        if self.question:
            database.update_question(self.question, self.edit_name.text(), self.edit_answer.toPlainText())
        else:
            database.insert_question(self.edit_name.text(), self.edit_answer.toPlainText())

        self.__show_popup()
        self.__on_back_button_clicked()

    def __show_popup(self):
        alert = QMessageBox()
        alert.setText("Question saved!")
        alert.exec_()

    def __setup_button(self, text):
        button = QPushButton(text)
        button.setFixedWidth(60)
        button.setAttribute(Qt.WA_StyledBackground, True)
        button.setStyleSheet("background-color: white")
        return button

    def __setup_edit_question_layout(self):
        edit_question_layout = QVBoxLayout()
        self.edit_name = QLineEdit(self.question_name)
        self.__setup_attribute(self.edit_name)
        edit_question_layout.addWidget(self.edit_name)
        self.edit_answer = QPlainTextEdit()
        if self.question:
            self.edit_answer.setEnabled(False)
        else:
            self.edit_answer.setEnabled(True)
        self.__setup_attribute(self.edit_answer)
        edit_question_layout.addWidget(self.edit_answer)
        self.layout.addLayout(edit_question_layout)

    def __setup_attribute(self, widget):
        widget.setAttribute(Qt.WA_StyledBackground, True)
        widget.setStyleSheet("background-color: white;")
