from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QPlainTextEdit, QMessageBox
from PyQt5.QtCore import Qt

from src.Presentation.Quiz.QuizViewModel import QuizViewModel


class QuizView(QWidget):
    def __init__(self):
        super().__init__()
        self.view_model = QuizViewModel()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: rgba(0, 41, 59, 255)")
        self.layout = QVBoxLayout()
        self.__setup_top_bar_buttons()
        self.__setup_show_question_layout()
        self.__connect_with_view_model()
        self.setLayout(self.layout)

    def __setup_top_bar_buttons(self):
        top_bar_layout = QHBoxLayout()
        self.result_label = QLabel('')
        self.__setup_attribute(self.result_label)
        self.start_show_answer_button = self.__setup_button('Start')
        self.start_show_answer_button.clicked.connect(self.__on_start_show_answer_clicked)
        self.incorrect_answer_button = self.__setup_button('NO')
        self.incorrect_answer_button.clicked.connect(self.__on_incorrect_answer_button_clicked)
        self.correct_answer_button = self.__setup_button('YES')
        self.correct_answer_button.clicked.connect(self.__on_correct_answer_button_clicked)
        top_bar_layout.addWidget(self.result_label)
        top_bar_layout.addWidget(self.start_show_answer_button)
        top_bar_layout.addWidget(self.incorrect_answer_button)
        top_bar_layout.addWidget(self.correct_answer_button)
        self.layout.addLayout(top_bar_layout)

    def __on_start_show_answer_clicked(self):
        if self.start_show_answer_button.text() == 'Start':
            self.__on_start_quiz()
        else:
            self.view_model.answer_for_question()

    def __on_start_quiz(self):
        self.start_show_answer_button.setText('Answer')
        self.view_model.on_start()

    def __on_incorrect_answer_button_clicked(self):
        self.view_model.was_incorrect_answer()
        self.view_model.next_question()

    def __on_correct_answer_button_clicked(self):
        self.view_model.was_correct_answer()
        self.view_model.next_question()

    def __on_showing_answer(self, answer):
        self.incorrect_answer_button.setEnabled(True)
        self.correct_answer_button.setEnabled(True)
        self.start_show_answer_button.setEnabled(False)
        self.answer_name.setPlainText(answer)

    def __on_showing_question(self, question):
        self.incorrect_answer_button.setEnabled(False)
        self.correct_answer_button.setEnabled(False)
        self.start_show_answer_button.setEnabled(True)
        self.question_name.setText(question)
        self.answer_name.setPlainText("")

    def __connect_with_view_model(self):
        self.view_model.current_result.connect(self.__update_result_label)
        self.view_model.question.connect(self.__show_question)
        self.view_model.answer.connect(self.__show_answer)

    def __update_result_label(self, result):
        self.result_label.setText(result)

    def __show_question(self, question):
        if question != "":
            self.__on_showing_question(question)
        else:
            self.incorrect_answer_button.setEnabled(False)
            self.correct_answer_button.setEnabled(False)
            self.__show_popup()
            self.start_show_answer_button.setText('Start')
            self.start_show_answer_button.setEnabled(True)

    def __show_answer(self, answer):
        self.__on_showing_answer(answer)

    def __show_popup(self):
        alert = QMessageBox()
        alert.setText(f"Quiz finished with result {self.result_label.text()}")
        alert.exec_()

    def __setup_button(self, text):
        button = QPushButton(text)
        button.setFixedWidth(60)
        button.setAttribute(Qt.WA_StyledBackground, True)
        button.setStyleSheet("background-color: white")
        return button

    def __setup_show_question_layout(self):
        show_question_layout = QVBoxLayout()
        self.question_name = QLineEdit("")
        self.__setup_attribute(self.question_name)
        show_question_layout.addWidget(self.question_name)
        self.answer_name = QPlainTextEdit()
        self.__setup_attribute(self.answer_name)
        show_question_layout.addWidget(self.answer_name)
        self.layout.addLayout(show_question_layout)

    def __setup_attribute(self, widget):
        widget.setAttribute(Qt.WA_StyledBackground, True)
        widget.setStyleSheet("background-color: white;")
