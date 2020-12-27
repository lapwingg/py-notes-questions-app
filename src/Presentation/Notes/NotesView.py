from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListView, QAbstractItemView, QMessageBox
from PyQt5.QtCore import Qt, QStringListModel

from src.Presentation.Notes.NoteDetailsView import NoteDetailsView


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
        self.remove_note_button = self.__setup_button('Remove', False)
        self.new_note_button = self.__setup_button('New', True)
        self.new_note_button.clicked.connect(self.__on_button_clicked_event)
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

    def __on_button_clicked_event(self):
        note_details = NoteDetailsView()
        note_details.setParent(self)
        note_details.setFixedWidth(self.width())
        note_details.setFixedHeight(self.height())
        note_details.show()

    def __setup_note_list_view(self):
        list_view = QListView()
        list_view.setModel(QStringListModel(["Note_0", "Note_1", "Note_2", "Note_3", "Note_4", "Note_5"]))
        list_view.setAttribute(Qt.WA_StyledBackground, True)
        list_view.setStyleSheet("background-color: white")
        list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        list_view.clicked.connect(self.__list_view_item_selected)
        self.layout.addWidget(list_view)

    def __list_view_item_selected(self):
        self.edit_note_button.setEnabled(True)
        self.remove_note_button.setEnabled(True)

    def __show_popup(self):
        alert = QMessageBox()
        alert.setText("One day, you will be able to filter data!")
        alert.exec_()
