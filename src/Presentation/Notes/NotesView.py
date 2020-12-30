from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListView, QAbstractItemView, QMessageBox
from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtGui import QShowEvent

from src.Presentation.Notes.NoteDetailsView import NoteDetailsView
from src.Database.Database import Database


class NotesView(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: rgba(0, 41, 59, 255)")
        self.layout = QVBoxLayout()
        self.__setup_top_bar()
        self.__setup_note_list_view()
        self.setLayout(self.layout)

    def __setup_top_bar(self):
        top_bar = QHBoxLayout()
        separator = QWidget()
        self.edit_note_button = self.__setup_button('Edit', False)
        self.edit_note_button.clicked.connect(self.__on_edit_button_clicked)
        self.remove_note_button = self.__setup_button('Remove', False)
        self.remove_note_button.clicked.connect(self.__on_remove_button_clicked)
        self.new_note_button = self.__setup_button('New', True)
        self.new_note_button.clicked.connect(self.__on_new_note_button_clicked)
        self.filter_note_button = self.__setup_button('Filter', True)
        self.filter_note_button.clicked.connect(self.__show_popup)
        top_bar.addWidget(separator)
        top_bar.addWidget(self.edit_note_button)
        top_bar.addWidget(self.remove_note_button)
        top_bar.addWidget(self.new_note_button)
        top_bar.addWidget(self.filter_note_button)
        self.layout.addLayout(top_bar)

    def __setup_button(self, text, enabled):
        button = QPushButton(text)
        button.setFixedWidth(60)
        button.setEnabled(enabled)
        button.setAttribute(Qt.WA_StyledBackground, True)
        button.setStyleSheet("background-color: white")
        return button

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
        self.list_view.setAttribute(Qt.WA_StyledBackground, True)
        self.list_view.setStyleSheet("background-color: white")
        self.list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_view.clicked.connect(self.__list_view_item_selected)
        self.layout.addWidget(self.list_view)

    def __list_view_item_selected(self, index):
        self.edit_note_button.setEnabled(True)
        self.remove_note_button.setEnabled(True)
        self.selected_index = index.row()

    def __show_popup(self):
        alert = QMessageBox()
        alert.setText("One day, you will be able to filter data!")
        alert.exec_()

    def showEvent(self, a0: QShowEvent) -> None:
        if a0 == QShowEvent.Show:
            self.layout.removeWidget(self.list_view)
            self.__setup_note_list_view()
            self.setLayout(self.layout)
