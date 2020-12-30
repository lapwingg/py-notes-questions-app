from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QShowEvent

from src.Database.Database import Database


class TechnologyDetailsView(QWidget):
    name = ""
    technology = None

    def __init__(self, technology=None):
        super().__init__()
        if technology:
            self.technology = technology
            self.name = self.technology.name

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: rgba(0, 41, 59, 255)")
        self.layout = QVBoxLayout()
        self.__setup_top_bar_buttons()
        self.__setup_edit_technology_layout()
        self.setLayout(self.layout)

    def __setup_top_bar_buttons(self):
        top_bar_layout = QHBoxLayout()
        widget = QWidget()
        widget2 = QWidget()
        back_button = self.__setup_button('Back')
        back_button.clicked.connect(self.__on_back_button_clicked)
        save_button = self.__setup_button('Save')
        save_button.clicked.connect(self.__on_save_button_clicked)
        top_bar_layout.addWidget(widget)
        top_bar_layout.addWidget(widget2)
        top_bar_layout.addWidget(back_button)
        top_bar_layout.addWidget(save_button)
        self.layout.addLayout(top_bar_layout)

    def __on_back_button_clicked(self):
        self.hide()
        self.parent().showEvent(QShowEvent.Show)

    def __on_save_button_clicked(self):
        database = Database()
        if self.technology:
            database.update_technology(self.technology, self.edit_name.text())
        else:
            database.insert_technology(self.edit_name.text())

        self.__show_popup()
        self.__on_back_button_clicked()

    def __show_popup(self):
        alert = QMessageBox()
        alert.setText("Technology saved!")
        alert.exec_()

    def __setup_button(self, text):
        button = QPushButton(text)
        button.setFixedWidth(60)
        button.setAttribute(Qt.WA_StyledBackground, True)
        button.setStyleSheet("background-color: white")
        return button

    def __setup_edit_technology_layout(self):
        edit_technology_layout = QVBoxLayout()
        self.edit_name = QLineEdit(self.name)
        self.__setup_attribute(self.edit_name)
        edit_technology_layout.addWidget(self.edit_name)
        widget = QWidget()
        edit_technology_layout.addWidget(widget)
        self.layout.addLayout(edit_technology_layout)

    def __setup_attribute(self, widget):
        widget.setAttribute(Qt.WA_StyledBackground, True)
        widget.setStyleSheet("background-color: white;")
