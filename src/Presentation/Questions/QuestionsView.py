from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListView, QAbstractItemView, QMessageBox
from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtGui import QShowEvent

from src.Presentation.Questions.QuestionDetailsView import QuestionDetailsView
from src.Database.Database import Database


class QuestionsView(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: rgba(0, 41, 59, 255)")
        self.layout = QVBoxLayout()
        self.__setup_top_bar()
        self.__setup_question_list_view()
        self.setLayout(self.layout)

    def __setup_top_bar(self):
        top_bar = QHBoxLayout()
        separator = QWidget()
        self.edit_question_button = self.__setup_button('Edit', False)
        self.edit_question_button.clicked.connect(self.__on_edit_button_clicked)
        self.remove_question_button = self.__setup_button('Remove', False)
        self.remove_question_button.clicked.connect(self.__on_remove_button_clicked)
        self.new_question_button = self.__setup_button('New', True)
        self.new_question_button.clicked.connect(self.__on_new_button_clicked)
        self.filter_question_button = self.__setup_button('Filter', True)
        self.filter_question_button.clicked.connect(self.__show_popup)
        top_bar.addWidget(separator)
        top_bar.addWidget(self.edit_question_button)
        top_bar.addWidget(self.remove_question_button)
        top_bar.addWidget(self.new_question_button)
        top_bar.addWidget(self.filter_question_button)
        self.layout.addLayout(top_bar)

    def __setup_button(self, text, enabled):
        button = QPushButton(text)
        button.setFixedWidth(60)
        button.setEnabled(enabled)
        button.setAttribute(Qt.WA_StyledBackground, True)
        button.setStyleSheet("background-color: white")
        return button

    def __on_edit_button_clicked(self):
        self.edit_question_button.setEnabled(False)
        self.remove_question_button.setEnabled(False)
        question = self.questions[self.selected_index]
        question_details = QuestionDetailsView(question)
        question_details.setParent(self)
        question_details.setFixedWidth(self.width())
        question_details.setFixedHeight(self.height())
        question_details.show()

    def __on_remove_button_clicked(self):
        self.edit_question_button.setEnabled(False)
        self.remove_question_button.setEnabled(False)
        question = self.questions[self.selected_index]
        self.database.delete_question(question)
        self.showEvent(QShowEvent.Show)

    def __on_new_button_clicked(self):
        question_details = QuestionDetailsView()
        question_details.setParent(self)
        question_details.setFixedWidth(self.width())
        question_details.setFixedHeight(self.height())
        question_details.show()

    def __setup_question_list_view(self):
        self.list_view = QListView()
        self.database = Database()
        self.questions = self.database.get_questions()
        self.list_view.setModel(QStringListModel([question.question for question in self.questions]))
        self.list_view.setAttribute(Qt.WA_StyledBackground, True)
        self.list_view.setStyleSheet("background-color: white")
        self.list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_view.clicked.connect(self.__list_view_item_selected)
        self.layout.addWidget(self.list_view)

    def __list_view_item_selected(self, index):
        self.edit_question_button.setEnabled(True)
        self.remove_question_button.setEnabled(True)
        self.selected_index = index.row()

    def __show_popup(self):
        alert = QMessageBox()
        alert.setText("One day, you will be able to filter data!")
        alert.exec_()

    def showEvent(self, a0: QShowEvent) -> None:
        if a0 == QShowEvent.Show:
            self.layout.removeWidget(self.list_view)
            self.__setup_question_list_view()
            self.setLayout(self.layout)
