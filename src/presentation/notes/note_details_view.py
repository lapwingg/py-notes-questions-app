"""note_details_view.py"""
from PyQt5.QtGui import QShowEvent

from src.database.database import Database
from src.presentation.qpresentation_widget import QPresentationWidget
from src.presentation.top_bar_producer import TopBarProducer


class NoteDetailsView(QPresentationWidget):
    """View representing a details of note"""
    name = ""
    description = ""
    note = None

    def __init__(self, note=None):
        super().__init__()
        if note:
            self.note = note
            self.name = self.note.name
            self.description = self.note.description

        self.__setup_top_bar_buttons()
        self.__setup_edit_note_layout()
        self.set_layout()

    def __setup_top_bar_buttons(self):
        back_note_button = self.produce_button('Back',
                                               on_clicked=self.__on_back_button_clicked)
        save_note_button = self.produce_button('Save',
                                               on_clicked=self.__on_save_button_clicked)
        top_bar_layout = TopBarProducer.produce_top_bar([back_note_button,
                                                         save_note_button])
        self.layout.addLayout(top_bar_layout)

    def __on_back_button_clicked(self):
        self.hide()
        self.parent().showEvent(QShowEvent.Show)

    def __on_save_button_clicked(self):
        database = Database()
        if self.note:
            database.update_note(self.note, self.edit_name.text(),
                                 self.edit_description.toPlainText())
        else:
            database.insert_note(self.edit_name.text(),
                                 self.edit_description.toPlainText())

        self.__show_popup()
        self.__on_back_button_clicked()

    def __show_popup(self):
        self.show_popup_with_text("Note saved!")

    def __setup_edit_note_layout(self):
        edit_note_layout = self.produce_vertical_layout()
        self.edit_name = self.produce_line_edit(self.name)
        self.edit_description = self.produce_plain_text_edit(self.description)
        edit_note_layout.addWidget(self.edit_name)
        edit_note_layout.addWidget(self.edit_description)
        self.layout.addLayout(edit_note_layout)
