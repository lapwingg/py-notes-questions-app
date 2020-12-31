"""questions_view.py"""
from PyQt5.QtWidgets import QListView, QAbstractItemView
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QShowEvent

from src.presentation.questions.question_details_view import QuestionDetailsView
from src.presentation.qpresentation_widget import QPresentationWidget
from src.database.database import Database


class QuestionsView(QPresentationWidget):
    """View representing Questions"""

    selected_index = -1

    def __init__(self):
        super().__init__()
        self.__setup_top_bar()
        self.__setup_question_list_view()
        self.set_layout()

    def __setup_top_bar(self):
        top_bar = self.produce_horizontal_layout()
        separator = self.produce_widget()
        self.edit_question_button = self.produce_button('Edit',
                                                        on_clicked=self.__on_edit_button_c,
                                                        enabled=False)
        self.remove_question_button = self.produce_button('Remove',
                                                          on_clicked=self.__on_remove_button_c,
                                                          enabled=False)
        self.new_question_button = self.produce_button('New',
                                                       on_clicked=self.__on_new_button_c,
                                                       enabled=True)
        filter_question_button = self.produce_button('Filter',
                                                          on_clicked=self.__show_popup,
                                                          enabled=True)
        top_bar.addWidget(separator)
        top_bar.addWidget(self.edit_question_button)
        top_bar.addWidget(self.remove_question_button)
        top_bar.addWidget(self.new_question_button)
        top_bar.addWidget(filter_question_button)
        self.layout.addLayout(top_bar)

    def __on_edit_button_c(self):
        self.edit_question_button.setEnabled(False)
        self.remove_question_button.setEnabled(False)
        question = self.questions[self.selected_index]
        question_details = QuestionDetailsView(question)
        question_details.setParent(self)
        question_details.setFixedWidth(self.width())
        question_details.setFixedHeight(self.height())
        question_details.show()

    def __on_remove_button_c(self):
        self.edit_question_button.setEnabled(False)
        self.remove_question_button.setEnabled(False)
        question = self.questions[self.selected_index]
        self.database.delete_question(question)
        self.showEvent(QShowEvent.Show)

    def __on_new_button_c(self):
        question_details = QuestionDetailsView()
        question_details.setParent(self)
        question_details.setFixedWidth(self.width())
        question_details.setFixedHeight(self.height())
        question_details.show()

    def __setup_question_list_view(self):
        self.list_view = QListView()
        self.database = Database()
        self.questions = self.database.get_questions()
        self.list_view.setModel(QStringListModel(
            [question.question for question in self.questions]
        ))
        self.setup_background_color_for_widget(self.list_view)
        self.list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_view.clicked.connect(self.__list_view_item_selected)
        self.layout.addWidget(self.list_view)

    def __list_view_item_selected(self, index):
        self.edit_question_button.setEnabled(True)
        self.remove_question_button.setEnabled(True)
        self.selected_index = index.row()

    def __show_popup(self):
        self.show_popup_with_text("One day, you will be able to filter data!")

    def showEvent(self, a0: QShowEvent) -> None:
        """Custom implementation of showEvent function"""
        if a0 == QShowEvent.Show:
            self.layout.removeWidget(self.list_view)
            self.__setup_question_list_view()
            self.setLayout(self.layout)
