from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListView, QAbstractItemView, QMessageBox
from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtGui import QShowEvent

from src.Presentation.Technologies.TechnologyDetailsView import TechnologyDetailsView
from src.Database.Database import Database


class TechnologiesView(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: rgba(0, 41, 59, 255)")
        self.layout = QVBoxLayout()
        self.__setup_top_bar()
        self.__setup_technology_list_view()
        self.setLayout(self.layout)

    def __setup_top_bar(self):
        top_bar = QHBoxLayout()
        separator = QWidget()
        self.edit_technology_button = self.__setup_button('Edit', False)
        self.edit_technology_button.clicked.connect(self.__on_edit_button_clicked)
        self.remove_technology_button = self.__setup_button('Remove', False)
        self.remove_technology_button.clicked.connect(self.__on_remove_button_clicked)
        self.new_technology_button = self.__setup_button('New', True)
        self.new_technology_button.clicked.connect(self.__on_new_button_clicked)
        self.filter_technology_button = self.__setup_button('Filter', True)
        self.filter_technology_button.clicked.connect(self.__show_popup)
        top_bar.addWidget(separator)
        top_bar.addWidget(self.edit_technology_button)
        top_bar.addWidget(self.remove_technology_button)
        top_bar.addWidget(self.new_technology_button)
        top_bar.addWidget(self.filter_technology_button)
        self.layout.addLayout(top_bar)

    def __setup_button(self, text, enabled):
        button = QPushButton(text)
        button.setFixedWidth(60)
        button.setEnabled(enabled)
        button.setAttribute(Qt.WA_StyledBackground, True)
        button.setStyleSheet("background-color: white")
        return button

    def __on_edit_button_clicked(self):
        self.edit_technology_button.setEnabled(False)
        self.remove_technology_button.setEnabled(False)
        technology = self.technologies[self.selected_index]
        technology_details = TechnologyDetailsView(technology)
        technology_details.setParent(self)
        technology_details.setFixedWidth(self.width())
        technology_details.setFixedHeight(self.height())
        technology_details.show()

    def __on_remove_button_clicked(self):
        self.edit_technology_button.setEnabled(False)
        self.remove_technology_button.setEnabled(False)
        technology = self.technologies[self.selected_index]
        self.database.delete_technology(technology)
        self.showEvent(QShowEvent.Show)

    def __on_new_button_clicked(self):
        technology_details = TechnologyDetailsView()
        technology_details.setParent(self)
        technology_details.setFixedWidth(self.width())
        technology_details.setFixedHeight(self.height())
        technology_details.show()

    def __setup_technology_list_view(self):
        self.list_view = QListView()
        self.database = Database()
        self.technologies = self.database.get_technologies()
        self.list_view.setModel(QStringListModel([technology.name for technology in self.technologies]))
        self.list_view.setAttribute(Qt.WA_StyledBackground, True)
        self.list_view.setStyleSheet("background-color: white")
        self.list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_view.clicked.connect(self.__list_view_item_selected)
        self.layout.addWidget(self.list_view)

    def __list_view_item_selected(self, index):
        self.edit_technology_button.setEnabled(True)
        self.remove_technology_button.setEnabled(True)
        self.selected_index = index.row()

    def __show_popup(self):
        alert = QMessageBox()
        alert.setText("One day, you will be able to filter data!")
        alert.exec_()

    def showEvent(self, a0: QShowEvent) -> None:
        if a0 == QShowEvent.Show:
            self.layout.removeWidget(self.list_view)
            self.__setup_technology_list_view()
            self.setLayout(self.layout)
