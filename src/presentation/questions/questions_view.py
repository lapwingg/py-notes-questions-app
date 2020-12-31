"""questions_view.py"""
from PyQt5.QtGui import QShowEvent

from src.presentation.questions.question_details_view import QuestionDetailsView
from src.presentation.qpresentation_widget import QPresentationWidget
from src.database.database import Database
from src.presentation.top_bar_producer import TopBarProducer


class QuestionsView(QPresentationWidget):
    """View representing Questions"""

    selected_index = -1

    def __init__(self):
        super().__init__()
        self.method_for_show_event(self.__setup_question_list_view)
        self.__setup_top_bar()
        self.__setup_question_list_view()
        self.set_layout()

    def __setup_top_bar(self):
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
        top_bar = TopBarProducer.produce_top_bar([self.edit_question_button,
                                                  self.remove_question_button,
                                                  self.new_question_button,
                                                  filter_question_button])
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
        self.list_view = self.produce_list_view(data_type=self.Questions,
                                                on_clicked=self.__list_view_item_selected)
        self.database = Database()
        self.questions = self.database.get_questions()
        self.layout.addWidget(self.list_view)

    def __list_view_item_selected(self, index):
        self.edit_question_button.setEnabled(True)
        self.remove_question_button.setEnabled(True)
        self.selected_index = index.row()

    def __show_popup(self):
        self.show_popup_with_text("One day, you will be able to filter data!")
