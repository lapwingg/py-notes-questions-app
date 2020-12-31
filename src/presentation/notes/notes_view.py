"""note_view.py"""
from PyQt5.QtWidgets import QListView, QAbstractItemView
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QShowEvent

from src.presentation.notes.note_details_view import NoteDetailsView
from src.presentation.qpresentation_widget import QPresentationWidget
from src.database.database import Database


class NotesView(QPresentationWidget):
    """View representing Notes"""

    selected_index = -1

    def __init__(self):
        super().__init__()
        self.__setup_top_bar()
        self.__setup_note_list_view()
        self.set_layout()

    def __setup_top_bar(self):
        top_bar = self.produce_horizontal_layout()
        separator = self.produce_widget()
        self.edit_note_button = self.produce_button('Edit',
                                                    on_clicked=self.__on_edit_button_clicked,
                                                    enabled=False)
        self.remove_note_button = self.produce_button('Remove',
                                                      on_clicked=self.__on_remove_button_clicked,
                                                      enabled=False)
        self.new_note_button = self.produce_button('New',
                                                   on_clicked=self.__on_new_note_button_clicked,
                                                   enabled=True)
        filter_note_button = self.produce_button('Filter',
                                                 on_clicked=self.__show_popup,
                                                 enabled=True)
        top_bar.addWidget(separator)
        top_bar.addWidget(self.edit_note_button)
        top_bar.addWidget(self.remove_note_button)
        top_bar.addWidget(self.new_note_button)
        top_bar.addWidget(filter_note_button)
        self.layout.addLayout(top_bar)

    def __on_edit_button_clicked(self):
        self.edit_note_button.setEnabled(False)
        self.remove_note_button.setEnabled(False)
        note = self.notes[self.selected_index]
        note_details = NoteDetailsView(note)
        note_details.setParent(self)
        note_details.setFixedWidth(self.width())
        note_details.setFixedHeight(self.height())
        note_details.show()

    def __on_remove_button_clicked(self):
        self.edit_note_button.setEnabled(False)
        self.remove_note_button.setEnabled(False)
        note = self.notes[self.selected_index]
        self.database.delete_note(note)
        self.showEvent(QShowEvent.Show)

    def __on_new_note_button_clicked(self):
        note_details = NoteDetailsView()
        note_details.setParent(self)
        note_details.setFixedWidth(self.width())
        note_details.setFixedHeight(self.height())
        note_details.show()

    def __setup_note_list_view(self):
        self.list_view = QListView()
        self.database = Database()
        self.notes = self.database.get_notes()
        self.list_view.setModel(QStringListModel([note.name for note in self.notes]))
        self.setup_background_color_for_widget(self.list_view)
        self.list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_view.clicked.connect(self.__list_view_item_selected)
        self.layout.addWidget(self.list_view)

    def __list_view_item_selected(self, index):
        self.edit_note_button.setEnabled(True)
        self.remove_note_button.setEnabled(True)
        self.selected_index = index.row()

    def __show_popup(self):
        self.show_popup_with_text("One day, you will be able to filter data!")

    def showEvent(self, a0: QShowEvent) -> None:
        """Custom implementation of showEvent function"""
        if a0 == QShowEvent.Show:
            self.layout.removeWidget(self.list_view)
            self.__setup_note_list_view()
            self.setLayout(self.layout)
