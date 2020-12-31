"""question_details_view.py"""
from PyQt5.QtGui import QShowEvent

from src.database.database import Database
from src.presentation.qpresentation_widget import QPresentationWidget


class QuestionDetailsView(QPresentationWidget):
    """View representing a question"""
    question_name = ""
    question_answer = ""
    question = None

    def __init__(self, question=None):
        super().__init__()
        if question:
            self.question = question
            self.question_name = self.question.question
            self.question_answer = self.question.answer

        self.__setup_top_bar_buttons()
        self.__setup_edit_question_layout()
        self.set_layout()

    def __setup_top_bar_buttons(self):
        top_bar_layout = self.produce_horizontal_layout()
        widget = self.produce_widget()
        show_answer_button = self.produce_button('Answer', on_clicked=self.__on_show_answer_clicked)
        back_button = self.produce_button('Back', on_clicked=self.__on_back_button_clicked)
        self.save_button = self.produce_button('Save', on_clicked=self.__on_save_button_clicked)
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
            database.update_question(self.question,
                                     self.edit_name.text(),
                                     self.edit_answer.toPlainText())
        else:
            database.insert_question(self.edit_name.text(),
                                     self.edit_answer.toPlainText())

        self.__show_popup()
        self.__on_back_button_clicked()

    def __show_popup(self):
        self.show_popup_with_text("Question saved!")

    def __setup_edit_question_layout(self):
        edit_question_layout = self.produce_vertical_layout()
        self.edit_name = self.produce_line_edit(self.question_name)
        edit_question_layout.addWidget(self.edit_name)
        self.edit_answer = self.produce_plain_text_edit('')
        if self.question:
            self.edit_answer.setEnabled(False)
        else:
            self.edit_answer.setEnabled(True)
        edit_question_layout.addWidget(self.edit_answer)
        self.layout.addLayout(edit_question_layout)
